#!/usr/bin/env python3
"""
Model for downloading pictures
"""

import xml.etree.ElementTree as ET
from model.commands.command import Command
from model.commands.upnp_client import Upnp_client

class Get_picture_list(Command):
    
    @staticmethod
    def execute(*args, **kwargs) -> bool:
        
        if not "count" in kwargs.keys():
            return False
        count = kwargs["count"]
        
        if "starting_index" in kwargs.keys():
            starting_index = kwargs["starting_index"]
        else:
            starting_index = 0
        
        if "filter_by" in kwargs.keys():
            filter_by = kwargs["filter_by"]
        else:
            filter_by = ""

        if "order_by" in kwargs.keys():
            order_by = kwargs["order_by"]
        else:
            order_by = ""
        
        upnp_client = Upnp_client.instance()
        answer = upnp_client.get_picture_overview(count, starting_index, filter_by, order_by)
        
        # create list from data
        
        return True
