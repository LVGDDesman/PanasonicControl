#!/usr/bin/env python3
"""
Inheritance Class for all executable commands
"""

from upnp_client import Upnp_client
from connection import Connection
from settings import Settings

class Command():
    
    def __init__(self):
        self = self
        self.connection = connection.instance()
        self.upnp_client = upnp_client.instance()
        self.settings = settings.instance()
        # not all Singletons are necessary for executing commands

    def execute():
        pass
