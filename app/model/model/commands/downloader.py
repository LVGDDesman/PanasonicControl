#!/usr/bin/env python3
"""
Model for downloading pictures
"""

import requests
from command import Command

class Downloader(Command):
    
    def get_preview(count, starting_index = 0, filter_by = "", order_by = ""):
        return self.upnp_client.get_picture_overview(count, starting_index, filter_by, order_by)

    """
    """
    def execute(*args):
        if not "picture" in args.keys() or not "folder" in args.keys():
            return False

        requesturl = "%s:%d/%s" % (self.connection.get_ip(), self.connection.get_download_port(), args["picture"])
        answer = requests.get(requesturl)
        
        if answer.status_code != 200:
            return False

        try:
            with open(args["file"], "wb+") as file:
                file.write(answer.content)
        except Exception as e:
            return False

        return True
