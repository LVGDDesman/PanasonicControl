#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
from .command import Command
from .settings import Settings
from .connection import Connection


class Get_setting(Command):
    """
    Object for the getsetting request
    """
    @staticmethod
    def execute(*args, **kwargs) -> bool:
        """
        Execute the getsetting request
        :param setting_type: the requested information
        :return: True, if successful, False otherwise. The data is stored in the settings object
        """

        if "setting_type" not in kwargs.keys():
            return False
        
        connection = Connection()
        settings = Settings()

        setting_type = kwargs["setting_type"]

        request_url = "http://%s:%d/cam.cgi?mode=getsetting&type=%s" %\
                (connection.server_ip, connection.http_port, setting_type)
        answer = requests.get(request_url)

        try:
            root = ET.fromstring(answer.text)

            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False
            
            if len(root.findall("settingvalue")) == 0 or setting_type not in root.findall("settingvalue")[0].attrib:
                return False

            setting_value = root.findall("settingvalue")[0].attrib[setting_type]

            settings.set_setting(setting_type, setting_value)
            
        except Exception as e:
            return False
        return True
