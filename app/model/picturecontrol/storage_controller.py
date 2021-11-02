from model.structures.download_structures import *
from model.commands.get_picturelist import Get_picture_list

class Storage_controller:
    
    def __init__(self):
        self._picture_store = Picture_store()

    def download_index(self):
        """
        This function is used to download a list of all pictures on the camera for the first time.
        :returns: True, if execution successful
        """
        data = Get_picture_list.execute(count = 50)
        picture_list = __parse_data(data["Result"])
        size = data["TotalMatches"]
        current_entry = len(picture_list)
        #TODO: Check

        self._picture_store.entry_count = size
        self._picture_store.update(picture_list, 0)
        
        while current_entry != size:
            download_size = min(size - current_entry, 50)

            data = Get_picture_list.execute(count = download_size, current_entry = current_entry)
            picture_list = __parse_data(data["Result"])
            
            #TODO: check
            self._picture_store.update(picture_list, current_entry)
            current_entry += len(picture_list)

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

    def __parse_response(self, data:str) -> list[picture_element]:
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
                size = info.attrib["size"]
                pic = Picture_data(name, size)
                variants["TSO".index(name[1])] = pic
            

            picture_container = Picture_info(title, variants[0], variants[1], variants[2])
            picture_list.append(picture_container)
    
        return picture_list
