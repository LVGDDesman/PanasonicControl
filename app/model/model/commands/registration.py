#!/usr/bin/env python3

import requests
from model.commands.command import Command
from model.commands.upnp_client import Upnp_client
from model.commands.connection import Connection

class Registration(Command):
    """
    Object for registering the client on the camera
    """
    @staticmethod
    def execute(*args) -> bool:
        """
        Executing the registration.
        -> initialisation via upnp
        -> registering to cam.cgi
        :param: None
        :return: True, if successful, False otherwise
        """
        
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
