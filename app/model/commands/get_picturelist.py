#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from .command import Command
from .command import command_response
from .upnp_client import Upnp_client

class Get_picture_list(Command):
    """
    Object for retrieving a picturelist from the camera
    """
    @staticmethod
    @command_response
    def execute(*args, **kwargs) -> bool:
        """
        Execute the upnp request to search pictures stored on the camera.
        :param count: any number, count of picturenames returned
        :param starting_index: <optional> number, where to start searching for pictures
        :param filter_by: <optional> filter the pictures by [ TODO ] 
        :param order_by: <optional> order the result by [TODO] 
        :return: True, if successful, False otherwise; the picturelist is passed on via events (TODO)
        """
        if not "count" in kwargs.keys():
            raise Command.err_param

        count = kwargs["count"]
        
        if "starting_index" in kwargs.keys():
            starting_index = kwargs["starting_index"]
        else:
            starting_index = 0  # TODO: check if 0 is first element
        
        if "filter_by" in kwargs.keys():
            filter_by = kwargs["filter_by"]
        else:
            filter_by = "*"

        if "order_by" in kwargs.keys():
            order_by = kwargs["order_by"]
        else:
            order_by = ""
        
        upnp_client = Upnp_client()
        answer = upnp_client.get_picture_overview(count, starting_index, filter_by, order_by)
        
        return answer
