#!/usr/bin/python

class Response():
    """
    object storing the response-information.
    """
    successful = True
    data = []
    error_message = ""
    
    def __init__(self, successful, data = [], error_message = ""):
        self = self
        self.sucessful = successful
        self.data = data
        self.error_message = error_message

    def get_successful(self):
        return self.successful

    def get_data(self):
        return self.data

    def get_error_message(self):
        return error_message

    def set_successful(self, sucessful):
        self.successful = successful

    def set_data(self, data):
        self.data = data

    def set_error_message(self, error_message):
        self.error_message = error_message
