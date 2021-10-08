#!/usr/bin/env python3
"""
Model for getsetting requests (i.e. configuration of the camera and connection
"""

import requests
import xml.etree.ElementTree as ET

class get_settings:
    
    def __init__(self, ip, setting_type = None):
        self = self
        self.ip = ip
        self.setting_type = setting_type
 
    def execute():
        requesturl = "%s/cam.cgi?mode=getsetting&value=%s" % (self.ip, self.setting_type)
        answer = requests.get(requesturl)

        try:
            root_node = ET.fromstring(answer.text).getroot()
            return root_node
        except Exception as e:
            raise
        return
    
    def set_ip(ip):
        self.ip = ip

    def get_ip():
        return self.ip

    def set_setting_type(setting_type):
        self.setting_type = setting_type

    def get_setting_type():
        return self.setting_type
