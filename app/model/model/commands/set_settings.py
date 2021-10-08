#!/usr/bin/env python3
"""
Model for setsettings requests (i.e. configure camera-settings)
"""

import requests
import xml.etree.ElementTree as ET

class get_settings:
    
    def __init__(self, ip, setting_type, value):
        self = self
        self.ip = ip
        self.setting_type = setting_type
        self.value = value

    def execute():
        requesturl = "%s/cam.cgi?mode=setsetting&type=%s&value=%s" % (self.ip, self.setting_type, self.value)
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
    
    def set_value(value):
        self.value = value

    def get_value():
        return self.value
