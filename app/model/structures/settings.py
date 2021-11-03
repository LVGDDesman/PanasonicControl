#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET
from .connection import Connection
from ..design_pattern.singleton import Singleton

class Settings(metaclass = Singleton):
    """
    Object that stores the camera settings locally
    Singleton
    """
    
    def __init__(self):
        self._settings = {}

    def get_setting(self, setting_type):
        """
        get setting value stored in this object
        :param setting_type: name of setting to retrieve
        :return: value of specified setting or False, if setting_type not in setting TODO
        """
        if setting_type not in self._settings:
            return False
        return self._settings[setting_type]

    def set_setting(self, setting_type, value):
        """
        set store key-value pair
        :param setting_type: key
        :param value: value
        """
        self._settings[setting_type] = value
