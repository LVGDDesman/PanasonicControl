#!/usr/bin/env python3
"""
"""

import requests
import xml.etree.ElementTree as ET
from command import Command

class Stop_stream(Command):

    def execute():
        requesturl = "%s:%d/cam.cgi?mode=stopstream" %\
            (self.connection.get_server_ip(), self.connection.get_http_port())
        answer = requests.get(requesturl)

        try:
            root = ET.fromstring(answer.text)

            if len(root.findall("result")) == 0 or root.findall("result")[0].text != "ok":
                return False

        except Exception as e:
            return False
        return True
