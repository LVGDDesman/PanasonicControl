import xml.etree.ElementTree as ET

from model.structures.download_structures import *
from controller.commands.get_picturelist import Get_picture_list
from controller.commands.downloader import Downloader

class Storage_controller:
    
    def __init__(self):
        self._picture_store = Picture_store()
        # TODO maybe we need a dict picture -> position for reverse easier lookup

    def download_index(self):
        """
        This function is used to download a list of all pictures on the camera for the first time.
        :returns: True, if execution successful
        """
        response = Get_picture_list.execute(count = 50)
        # check data successful
        if response.successful != True:
            print(response.error_message)
        
        data = response.data
        picture_list = self.__parse_response(data["Result"])
        size = data["TotalMatches"]
        current_entry = len(picture_list)
        #TODO: Check

        self._picture_store.update_segment(picture_list, 0)
        

        while current_entry != size:
            download_size = min(size - current_entry, 50)

            data = Get_picture_list.execute(count = download_size, starting_index = current_entry)
            picture_list = self.__parse_response(data.data["Result"])
            
            #TODO: check
            self._picture_store.update_segment(picture_list, current_entry)
            current_entry += len(picture_list)
        
        self._picture_store.entry_count = size
        
        return True 

    def download_all(self,folder, quality) -> bool:
        # TODO: it seems like you cant download longer than ~5 seconds...
        # need a refresh?
        for i in range(len(self._picture_store.picture_list)):
            picture = self._picture_store.picture_list[i]

            download = None
            if quality == "thumbnail":
                download = picture.thumbnail
            elif quality == "medium":
                download = picture.medium
            elif quality == "original":
                download = picture.original
            else:
                raise Exception("Quality "+quality+" not supported")
            
            wakeup = Get_picture_list.execute(count=1, starting_index=i)

            data = Downloader.execute(picture = download.name)
            if data.successful != True:
                print(data.error_message, download.name)
                # TODO error handling
                continue
                
            
            with open(folder + download.name, "wb+") as file:
                file.write(data.data)
        return True


    def download_image(self, name, folder, quality) -> bool:
        picture = None
        for picture in self._picture_store.picture_list:
            if picture.name == name:
                break
        
        download = None
        if quality == "thumbnail":
            download = picture.thumbnail
        elif quality == "medium":
            download = picture.medium
        elif quality == "original":
            download = picture.original
        else:
            raise Exception("Quality "+quality+" not supported")
        
        data = Downloader.execute(picture = download.name)
        if data.successful != True:
            print(data.error_message)
            # TODO error handling
            return False
            
        with open(folder + download.name, "wb+") as file:
            file.write(data.data)

        return True


    def update_index(self) -> bool:
        """
        update pictureindex
        :return: True, if execution successful
        """
        
        return 

    def download_thumbnails(self):
        """
        Download thumbnails for all pictures currently stored in the picture_list 
        :return: True, if successful
        """
        for picture in self._picture_store.picture_list:
            picture_blob = Downloader.execute(picture.thumbnail.name)
            # check
            picture.thumbnail.data = picture_blob
        return True

    def __parse_response(self, data:str) -> list[Picture_info]:
        """
        This function __parses the xml data and creates a list of pictures
        :param data: the xml string response of the camera
        :return: list of picture_elements
        """
        picture_list = []

        root = ET.fromstring(data)
        for element in root:
            variants = {}
            
            title = element.find("{http://purl.org/dc/elements/1.1/}title").text
            
            for result in element.findall("{urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/}res"):
                name = result.text.split("/")[-1]
                size = result.attrib["size"]
                pic = Picture_data(name, size)
                variants["TSO".index(name[1])] = pic
            

            picture_container = Picture_info(title, variants[0], variants[1], variants[2])
            picture_list.append(picture_container)
    
        return picture_list
