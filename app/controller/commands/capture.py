#!/usr/bin/env python3

# TODO Throw error in event queue (@ return False)

import requests
import xml.etree.ElementTree as ET

from .command import Command
from .command import command_response
from model.structures.connection import Connection as Connection


class Capture(Command):
    """
    Object that represents the capture-request.
    """

    @staticmethod
    @command_response
    def execute(*args, **kwargs):
        """
        Execute the capture request
        :return: True, if successful, False otherwise
        """
        connection = Connection()

        request_url = "http://%s:%d/cam.cgi?mode=camcmd&value=capture" % \
                      (connection.server_ip, connection.http_port)
        answer = requests.get(request_url)

        root = ET.fromstring(answer.text)

        if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
            raise Command.err_not_successful
        return None
