#!/usr/bin/env python3
"""
"""

import requests
from command import Command
from upnp_client import Upnp_client
from connection import Connection

class Registration(Command):

    def execute(*args) -> bool:
        
        upnp_client = Upnp_client.instance()
        connection = Connection.instance()

        if not upnp_client.initiate_registration():
            return False
        
        requesturl = "%s:%d/cam.cgi?mode=accctrl&&type=req_acc&value=%s&value2" %\
            (connection.get_server_ip(), connection.get_http_port,\
                    connection.get_uuid(), connection.get_client_name())
        
        answer = requests.get(requesturl)
        
        if not "ok" in answer:
            return False
        
        # parse / evaluate answer maybe? 
        # -> remote and encrypted might be important
        # but which part is encrypted?
        # Example: ok,G81-69497D,remote,encrypted
        return True
