#!/usr/bin/env python3

import requests
from .command import Command
from .connection import Connection

class Downloader(Command):
    """
    Object for downloading pictures
    """
    @staticmethod
    def execute(*args, **kwargs) -> bool:
        """
        Execute the download request 
        :param picture: name of picture to download 
        :param folder: local folder to save picture to (using the same name)
        :return: True, if successful, False otherwise
        """
        if not "picture" in kwargs.keys() or not "folder" in kwargs.keys():
            return False

        connection = Connection()

        requesturl = "http://%s:%d/%s" % (connection.server_ip, connection.download_port, kwargs["picture"])
        answer = requests.get(requesturl)
        
        if answer.status_code != 200:
            return False

        try:
            # TODO proper os path generation necessary
            path = kwargs["folder"] + kwargs["picture"]

            with open(path, "wb+") as file:
                file.write(answer.content)
        except Exception as e:
            return False

        return True
