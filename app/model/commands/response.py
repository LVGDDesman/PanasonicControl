#!/usr/bin/python
from typing import List

class Response:
    """
    object storing the response-information.
    """

    def __init__(self, successful: bool, data=None, error_message: str = None):
        self._successful = successful
        self._data = data
        self._error_message = error_message

    @property
    def successful(self):
        return self._successful

    @property
    def data(self):
        return self._data

    @property
    def error_message(self):
        return self._error_message

    @successful.setter
    def successful(self, successful):
        self._successful = successful

    @data.setter
    def data(self, data):
        self._data = data

    @error_message.setter
    def error_message(self, error_message):
        self._error_message = error_message
