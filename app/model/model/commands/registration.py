#!/usr/bin/env python3
"""
"""

import requests
from command import Command

class Registration(Command):

    """
    """
    def execute():
        
        if not self.upnp_client.initiate_registration():
            return False
        
        requesturl = "%s:%d/cam.cgi?mode=accctrl&&type=req_acc&value=%s&value2" %\
            (self.connection.get_server_ip(), self.connection.get_http_port,\
                    self.connection.get_uuid(), self.connection.get_client_name())
        
        answer = requests.get(requesturl)
        
        if not "ok" in answer:
            return False
        
        # parse / evaluate answer maybe? 
        # -> remote and encrypted might be important
        # but which part is encrypted?
        # Example: ok,G81-69497D,remote,encrypted
        return True
