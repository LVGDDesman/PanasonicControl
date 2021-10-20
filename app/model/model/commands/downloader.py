#!/usr/bin/env python3
"""
Model for downloading pictures
"""

import requests
from command import Command
from connection import Connection

class Downloader(Command):
    
    def execute(*args) -> bool:

        if not "picture" in args.keys() or not "folder" in args.keys():
            return False

        connection = Connection.instance()

        requesturl = "%s:%d/%s" % (connection.get_ip(), connection.get_download_port(), args["picture"])
        answer = requests.get(requesturl)
        
        if answer.status_code != 200:
            return False

        try:
            # TODO proper os path generation necessary
            path = args["folder"] + args["picture"]

            with open(path, "wb+") as file:
                file.write(answer.content)
        except Exception as e:
            return False

        return True
