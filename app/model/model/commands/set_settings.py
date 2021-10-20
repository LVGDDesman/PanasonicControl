#!/usr/bin/env python3
"""
Model for retrieval and adjustment of the cameraconfiguration and connection
"""

# TODO Throw error in event queue (@ return False)

import requests
import xml.etree.ElementTree as ET
from command import Command
from connection import Connection

class Set_setting(Command):
    
    def execute(*args) -> bool:
        if "setting_type" not in args.keys() or "setting_value" not in args.keys() :
            return False
        

        connection = Connection.instance()
        setting_type = args["setting_type"]
        setting_value = args["setting_value"]

        request_url = "%s:%d/cam.cgi?mode=setsetting&type=%s&value=%s" %\
                (connection.get_server_ip(), connection.get_http_port(), setting_type, setting_value)
        answer = requests.get(requesturl)

        try:
            root_node = ET.fromstring(answer.text)

            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False
            
        except Exception as e:
            return False
        return True
