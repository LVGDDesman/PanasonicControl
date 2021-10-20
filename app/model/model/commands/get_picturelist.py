#!/usr/bin/env python3
"""
Model for downloading pictures
"""

import xml.etree.ElementTree as ET
from command import Command
from upnp_client import Upnp_client

class Get_picture_list(Command):
    
    def execute(*args) -> bool:
        
        if not "count" in args.keys():
            return False
        count = args["count"]
        
        if "starting_index" in args.keys():
            starting_index = args["starting_index"]
        else:
            starting_index = 0
        
        if "filter_by" in args.keys():
            filter_by = args["filter_by"]
        else:
            filter_by = ""

        if "order_by" in args.keys():
            order_by = args["order_by"]
        else:
            order_by = ""
        
        upnp_client = Upnp_client.instance()
        answer = upnp_client.get_picture_overview(count, starting_index, filter_by, order_by)
        
        # create list from data
        
        return True
