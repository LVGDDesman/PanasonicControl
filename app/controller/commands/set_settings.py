#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
from .command import Command
from .command import command_response
from model.structures.connection import Connection as Connection

class Set_setting(Command):
    """
    Object, that represents the setsetting-request
    """
    @staticmethod
    @command_response
    def execute(*args, **kwargs) -> bool:
        """
        Execute the setsetting-request
        :param setting_type: name of setting, that is to be updated
        :param setting_value: new value of setting
        :return: True, if successful, False otherwise
        """

        if "setting_type" not in kwargs.keys() or "setting_value" not in kwargs.keys() :
            raise Command.err_param

        connection = Connection()
        setting_type = kwargs["setting_type"]
        setting_value = kwargs["setting_value"]

        request_url = "http://%s:%d/cam.cgi?mode=setsetting&type=%s&value=%s" %\
                (connection.server_ip, connection.http_port, setting_type, setting_value)
        answer = requests.get(request_url)
        try:
            root = ET.fromstring(answer.text)
            
            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                raise Command.err_not_successful
        except Exception as e:
            raise Command.err_not_successful
        
        return None
