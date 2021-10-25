#!/usr/bin/env python3
"""
"""

import requests
import xml.etree.ElementTree as ET
from model.commands.command import Command
from model.commands.connection import Connection

class Start_stream(Command):
    
    @staticmethod
    def execute(*args) -> bool:
        connection = Connection.instance()

        request_url = "http://%s:%d/cam.cgi?mode=startstream&value=%s" %\
            (connection.get_server_ip(), connection.get_http_port(), connection.get_stream_port() )
        answer = requests.get(request_url)

        try:
            root = ET.fromstring(answer.text)
            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False
        except Exception as e:
            return False
        return True
