#!/usr/bin/env python3
"""
"""

# TODO Throw error in event queue (@ return False)

import requests
import xml.etree.ElementTree as ET
from command import Command

class Capture(Command):
    
    def execute(*args):
        
        request_url = "%s:%d/cam.cgi?mode=camcmd&value=capture" %\
                (self.connection.get_server_ip(), self.connection.get_http_port())
        answer = requests.get(requesturl)

        try:
            root_node = ET.fromstring(answer.text)

            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False
            
        except Exception as e:
            return False
        return True
