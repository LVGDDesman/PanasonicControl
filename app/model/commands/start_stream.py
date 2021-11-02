#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
from .command import Command
from .command import command_response
from .connection import Connection

class Start_stream(Command):
    """
    Object, that represents the start-stream request
    """
    @staticmethod
    @command_response
    def execute(*args) -> bool:
        """
        Execute the start-strean request
        :return: True, if successful, False otherwise
        """
        connection = Connection()

        request_url = "http://%s:%d/cam.cgi?mode=startstream&value=%s" %\
            (connection.server_ip, connection.http_port, connection.stream_port )
        answer = requests.get(request_url)

        try:
            root = ET.fromstring(answer.text)
            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                raise Command.err_not_successful
        except Exception as e:
            raise Command.err_not_successful
        return None
