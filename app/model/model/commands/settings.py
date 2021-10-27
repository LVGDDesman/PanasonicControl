#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
from model.commands.connection import Connection

class Settings():
    """
    Object that stores the camera settings locally
    Singleton
    """
    _instance = None
    settings = {}
    
    def __init__(self):
        """
        __init__ is not alowed!
        """
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        """
        get instance of the settings-object
        :return: instance of (new) settings-object
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.connection = Connection.instance()
        
        return cls._instance

    def get_setting(self, setting_type):
        """
        get setting value stored in this object
        :param setting_type: name of setting to retrieve
        :return: value of specified setting or False, if setting_type not in setting TODO
        """
        if setting_type not in self.settings:
            return False
        return self.settings[setting_type]

    def set_setting(self, setting_type, value):
        """
        set store key-value pair
        :param setting_type: key
        :param value: value
        """
        self.settings[setting_type] = value
