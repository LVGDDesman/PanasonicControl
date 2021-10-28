#!/usr/bin/env python3

from .connection import Connection
from model.design_pattern.singleton import Singleton
import upnpy

class Upnp_client(metaclass = Singleton):
    """
    Object for upnp requests (i.e. Login, Mediacontrol)
    """
    
    def __init__(self):
        """
        """
        self._camera = None
        self._connection = Connection()

    def initiate_registration(self) -> bool:
        """
        Search for the camera-device.
        This function *has* to be called before other requests are send to the camera
        :return: True/False if camera was found
        """
        upnp = upnpy.UPnP()
        devices = upnp.discover()
        for device in devices:
            if device.get_friendly_name() == self._connection.get_server_name():
            # This is currently for one camera, needs to be changed for different cameras
                self._camera = device
                break

        if self._camera == None:
            return False
        
        uuid = self._camera.response.split("uuid:")[1].split(":")[0]
        # ugly, but i don't know how to do it better
        # upnpy doesn't seem to directly support reading the response of the discovery-request
        if uuid != None:
            self._connection.set_uuid(uuid)
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

        answer = self._camera.ContentDirectory.Browse(
                ObjectID=0, # not necessary right
                BrowseFlag='BrowseDirectChildren',
                Filter=filter_by,
                StartingIndex=starting_index,
                RequestedCount=count,
                SortCriteria=order_by
                )
        # create list from XML
        return answer
    
    @property
    def camera(self):
        """
        get upnp object of camera 
        :return: upnp object of camera
        """
        return self._camera
    
    @camera.setter
    def camera(self, camera):
        """
        set camera object
        :param camera: upnp camera object
        """
        self._camera = camera
