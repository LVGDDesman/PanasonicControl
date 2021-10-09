#!/usr/bin/env python3
"""
"""

# TODO Throw error in event queue (@ return False)

import requests
import xml.etree.ElementTree as ET
from command import Command

class Get_setting(Command):
    
    def execute(*args):
        if "setting_type" not in args.keys():
            return False
        
        setting_type = args["setting_type"]

        request_url = "%s:%d/cam.cgi?mode=getsetting&value=%s" %\
                (self.connection.get_server_ip(), self.connection.get_http_port(), setting_type)
        answer = requests.get(requesturl)

        try:
            root_node = ET.fromstring(answer.text)

            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False
            
            if len(root.findall("settingvalue")) == 0 or setting_type not in root.findall("settingvalue")[0].attrib:
                return False

            setting_value = root.findall("settingvalue")[0].attrib[setting_type]
            self.settings.set(setting_type, setting_value)
            
        except Exception as e:
            return False
        return True
