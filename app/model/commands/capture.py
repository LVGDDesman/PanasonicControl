#!/usr/bin/env python3

# TODO Throw error in event queue (@ return False)

import requests
import xml.etree.ElementTree as ET

from .command import Command
from .connection import Connection

class Capture(Command):
    """
    Object that represents the capture-request.
    """
    @staticmethod
    def execute(*args) -> bool:
        """
        Execute the capture request
        :return: True, if successful, False otherwise
        """
        connection = Connection()
            
        request_url = "http://%s:%d/cam.cgi?mode=camcmd&value=capture" %\
                (connection.server_ip, connection.http_port)
        answer = requests.get(request_url)

        try:
            root = ET.fromstring(answer.text)

            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False
            
        except Exception as e:
            return False
        return True
