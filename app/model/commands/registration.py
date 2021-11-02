#!/usr/bin/env python3

import requests
from .command import Command
from .command import command_response
from .upnp_client import Upnp_client
from .connection import Connection
from .set_settings import Set_setting
from .get_settings import Get_setting

class Registration(Command):
    """
    Object for registering the client on the camera
    """
    @staticmethod
    @command_response
    def execute(*args) -> bool:
        """
        Executing the registration.
        -> initialisation via upnp
        -> registering to cam.cgi
        :param: None
        :return: True, if successful, False otherwise
        """
        
        upnp_client = Upnp_client()
        connection = Connection()

        if not upnp_client.initiate_registration():
            raise Command.err_not_successful
        
        request_url = "http://%s:%d/cam.cgi?mode=accctrl&type=req_acc&value=%s&value2=%s" %\
            (connection.server_ip, connection.http_port,\
                    connection.uuid, connection.client_name)
        
        answer = requests.get(request_url)
        if not "ok" in answer.text:
            raise Command.err_not_successful
        
        Set_setting.execute(setting_type = "device_name", value = connection.client_ip)
        Get_setting.execute(setting_type = "pa")
        
        # parse / evaluate answer maybe? 
        # -> remote and encrypted might be important
        # but which part is encrypted?
        # Example: ok,G81-69497D,remote,encrypted
        return None
