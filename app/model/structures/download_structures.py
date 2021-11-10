from model.design_pattern.singleton import Singleton

class Picture_data():
    def __init__(self, name: str, size: int, data = None):
        self._name = name
        self._size = size
        self._data = data
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
class Picture_info:
    def __init__(self, name: str, thumbnail: Picture_data, medium: Picture_data, original: Picture_data):
        self._name = name
        self._thumbnail = thumbnail
        self._medium = medium
        self._original = original
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        self._thumbnail = thumbnail

    @property
    def medium(self):
        return self._medium
    
    @medium.setter
    def medium(self, medium):
        self._medium = medium
    
    @property
    def original(self):
        return self._original
    
    @original.setter
    def original(self, original):
        self._original = original

class Picture_store(metaclass = Singleton):
    """
    This object represents the overview over all pictures and their information.
    """

    def __init__(self, entry_count:int = 0, pictures = []):
            self._entry_count = entry_count 
            self._picture_list = pictures

    def check_segment_difference(self, segment:list, offset:int):
        """
        check if the specified part of the picturelist needs to be updated
        if it doesn't, all elements before don't need to be checked either
        :
        :return: True, if segments are different
        """
        end = len(segment)
        if offset > self._entry_count or offset + end > self._entry_count:
            return True

        if segment[end] != self._picture_list[offset + end]:
            return True

        if segment[0] != self._picture_list[offset]:
            return True 

        return False


    def update_segment(self, segment:list, offset:int):
        """
        This function updates a segment of the picturelist and replaces all elements in the specified segment with the actual elements.
        When updating a segment, the previous segment needs to exist beforehand (or it's the first)
        :param pictures: list of new picture_element's, which need to 
        :param offset: location of the segment in the whole 
        """
        
        if len(self._picture_list) < offset:
            raise Exception("Initialize previous Segment first!")
        
        for i in range(len(segment)):
            
            if offset + i >= self._entry_count:
                self._picture_list.append(segment[i])
            else:
                self._picture_list[offset + i ] = segment[i]

    @property
    def picture_list(self):
        return self._picture_list
    
    @picture_list.setter
    def picture_list(self, picture_list):
        self._picture_list = picture_list
    
    @property
    def entry_count(self):
        return self._entry_count
    
    @entry_count.setter
    def entry_count(self, entry_count):
        self._entry_count = entry_count
