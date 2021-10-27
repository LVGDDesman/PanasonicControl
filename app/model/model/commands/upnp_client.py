#!/usr/bin/env python3

from model.commands.connection import Connection
import upnpy

class Upnp_client():
    """
    Object for upnp requests (i.e. Login, Mediacontrol)
    Singleton
    """
    _instance = None
    connection = None
    camera = None

    def __init__(self):
        """
        __init__ is not allowed
        """
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        """
        return (new) instance of this object
        :return: instance of Upnp_client
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.connection = Connection.instance()
        
        return cls._instance
    
    def initiate_registration(self) -> bool:
        """
        Search for the camera-device.
        This function *has* to be called before other requests are send to the camera
        :return: True/False if camera was found
        """
        upnp = upnpy.UPnP()
        devices = upnp.discover()
        for device in devices:
            if device.get_friendly_name() == self.connection.get_server_name():
            # This is currently for one camera, needs to be changed for different cameras
                self.camera = device
                break

        if self.camera == None:
            return False
        print(self.camera.response)
        uuid = self.camera.response.split("uuid:")[1].split(":")[0]
        # ugly, but i don't know how to do it better
        # upnpy doesn't seem to directly support reading the response of the discovery-request
        if uuid != None:
            self.connection.set_uuid(uuid)
            return True
        return False

    def get_picture_overview(self, count, starting_index = 0, filter_by = None, order_by = None):
        """
        Execute the upnp request to search pictures stored on the camera.
        :param count: any number, count of picturenames returned
        :param starting_index: <optional> number, where to start searching for pictures
        :param filter_by: <optional> filter the pictures by [ TODO ]
        :param order_by: <optional> order the result by [TODO]
        :return: True, if successful, False otherwise; the picturelist is passed on via events (TODO)
        """

        answer = self.camera.ContentDirectory.Browse(
                ObjectID=0, # not necessary right
                BrowseFlag='BrowseDirectChildren',
                Filter=filter_by,
                StartingIndex=starting_index,
                RequestedCount=count,
                SortCriteria=order_by
                )
        # create list from XML
        return answer
    
    def get_camera(self):
        """
        get upnp object of camera 
        :return: upnp object of camera
        """
        return self.get_camera

    def set_camera(self,camera):
        """
        set camera object
        :param camera: upnp camera object
        """
        self.camera = camera
