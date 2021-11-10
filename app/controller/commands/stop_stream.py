#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
from .command import Command
from .command import command_response
from model.structures.connection import Connection as Connection

class Stop_stream(Command):
    """
    Object that represents the stop-stream request
    """
    @staticmethod
    @command_response
    def execute(*args) -> bool:
        """
        Execute the stop-stream request
        :return: True, if successful, False otherwise
        """
        connection = Connection()

        requesturl = "http://%s:%d/cam.cgi?mode=stopstream" %\
            (connection.server_ip, connection.http_port)
        answer = requests.get(requesturl)

        try:
            root = ET.fromstring(answer.text)
        except Exception as e:
             raise Command.err_not_successful
        
        if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
            raise Command.err_not_successful
        
        return None
