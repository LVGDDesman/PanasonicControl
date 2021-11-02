import unittest
from unittest import mock

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Modules to test

from model.commands.response import Response
from model.commands.connection import Connection
from model.commands.upnp_client import Upnp_client
from model.commands.settings import Settings
from model.commands.command import Command

from model.commands.capture import Capture
from model.commands.registration import Registration
from model.commands.downloader import Downloader
from model.commands.get_picturelist import Get_picture_list
from model.commands.get_settings import Get_setting
from model.commands.set_settings import Set_setting
from model.commands.start_stream import Start_stream
from model.commands.stop_stream import Stop_stream

Connection().initialize_g81_dmc()

print("login")
response = Registration.execute()
print(response.successful)
print(response.error_message)

print("get_pictures")
response = Get_picture_list.execute(count=20)
print(response)
exit()
print("capture")
response = Capture.execute()
print(response.successful)

print("startstream")
response = Start_stream.execute()
print(response.successful)

print("stopstream")
response = Stop_stream.execute()
print(response.successful)

print("download")
response = Downloader.execute(picture="TEST.jpg", folder=".output/")
print(response.successful)


print("get_setting")
response = Get_setting.execute(setting_type="shtrspeed")
print(response.successful)

print("set_setting")
response = Set_setting.execute(setting_type="shtrspeed", setting_value="2390/256")
print(response.successful)
