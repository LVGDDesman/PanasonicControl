#!/usr/bin/env python3

import requests
from .command import Command
from .command import command_response
from .connection import Connection

class Downloader(Command):
    """
    Object for downloading pictures
    """
    
    @staticmethod
    @command_response
    def execute(*args, **kwargs) -> bool:
        """
        Execute the download request 
        :param picture: name of picture to download 
        :param folder: local folder to save picture to (using the same name)
        :return: True, if successful, False otherwise
        """
        if not "picture" in kwargs.keys() or not "folder" in kwargs.keys():
            raise Command.err_param

        connection = Connection()

        requesturl = "http://%s:%d/%s" % (connection.server_ip, connection.download_port, kwargs["picture"])
        answer = requests.get(requesturl)
        
        if answer.status_code != 200:
            raise Command.err_not_successful

        try:
            # TODO proper os path generation necessary
            path = kwargs["folder"] + kwargs["picture"]

            with open(path, "wb") as file:
                file.write(answer.content)
        except Exception as e:
            raise Command.err_file

        return None
