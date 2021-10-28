import unittest
from nose.tools import assert_is_not_none
from unittest import mock

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Modules to test
import model.commands as Commands

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


def mocked_requests_get(*args, **kwargs):

    uuid = "XXXXXX-XXX"

    getsetting = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"\
            "<camrply><result>ok</result><settingvalue {}=\"{}\"></settingvalue></camrply>"

    class MockResponse:
        def __init__(self, text = "", status_code = 404, content = ""):
            self.text = text
            self.status_code = status_code
            self.content = content

        def text(self):
            return self.text

        def content(self):
            return self.content
    
    # Ready:
    ## Capture 
    if args[0] == 'http://192.168.54.1:80/cam.cgi?mode=camcmd&value=capture':
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)
    # Start Stream
    if args[0] == 'http://192.168.54.1:80/cam.cgi?mode=startstream&value=' + \
            str(Connection.instance().get_stream_port()):
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)
    # Stop Stream 
    if args[0] == 'http://192.168.54.1:80/cam.cgi?mode=stopstream':
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)
    ## set Settings
    elif 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=shtrspeed&value=' in args[0]\
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=iso&value=' in args[0]\
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=focal&value=' in args[0]\
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=exposure&value=' in args[0]\
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=whitebalance&value=' in args[0]:
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)

    ## Autofocus
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=camcmd&value=oneshot_a':
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)
    
    ## get Picturelist
    elif args[0] ==  'http://192.168.54.1:60606/Server0/CDS_control':
        with open("answers/picturelist.xml", "r") as file:
            return MockResponse(file.read(), 200)

    ## Download pictures
        
    elif args[0] == 'http://192.168.54.1:50001/TEST.jpg':
        with open("answers/TEST.jpg", "rb") as file:
            return MockResponse(status_code = 200, content = file.read())
    
    #WIP:
    elif args[0] == 'http://192.168.54.1:60606/Server0/CMS_event':
        return MockResponse(uuid, 200)
    
    elif args[0] == 'http://192.168.54.1/cam.cgi?mode=accctrl&type=req_acc&value='+uuid+'&value2=RNEL21':
        return MockResponse("", 200)
    
    ## get Settings
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=shtrspeed':
        return MockResponse(getsetting.format("shtrspeed", "2390/256"), 200)
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=iso':
        return MockResponse(getsetting.format("iso", "800"), 200)
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=focal':
        return MockResponse(getsetting.format("focal", "925/256"), 200)
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=exposure':
        return MockResponse(getsetting.format("shtrspeed", "1"), 200) # NOT RIGHT
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=whitebalance':
        return MockResponse(getsetting.format("whitebalane", "auto"), 200)
    print(args[0])   
    return MockResponse("", 404)

class Tests(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_commmand(self, mock_get):
        
        response = Command.execute()
        self.assertEqual(response, False)    

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_settings(self, mock_get):
        setting_name = "Test"
        setting_value = 100
        
        settings = Settings.instance()
        settings.set_setting(setting_name, setting_value)
        response = settings.get_setting(setting_name)

        self.assertEqual(setting_value, response)    

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_upnp_client(self, mock_get):
        # NOT WORKING
        upnp_client = Upnp_client.instance() 
        response = upnp_client.execute()
        self.assertEqual(response, True)
        return

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_capture(self, mock_get):
        response = Capture.execute()

        self.assertEqual(response, True)
    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_start_stream(self, mock_get):
        response = Start_stream.execute()

        self.assertEqual(response, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_stop_stream(self, mock_get):
        response = Stop_stream.execute()

        self.assertEqual(response, True)
    
    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_downloader(self, mock_get):
        response = Downloader.execute(picture = "TEST.jpg", folder = ".output/")

        self.assertEqual(response, True)
    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_picture_list(self, mock_get):
        Upnp_client.instance().initiate_registration()
        response = Get_picture_list.execute(count=20)

        self.assertEqual(response, True)
    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_setting(self, mock_get):
        response = Get_setting.execute(setting_type = "shtrspeed")

        self.assertEqual(response, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_registration(self, mock_get):
        response = Registration.execute()
        self.assertEqual(response, True)
        return

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_set_setting(self, mock_get):
        response = Set_setting.execute(setting_type = "shtrspeed", setting_value = "2390/256")

        self.assertEqual(response, True)



if __name__ == "__main__":
    connection = Connection.instance()
    upnp_client = Upnp_client.instance()
    connection.initialize_g81_dmc()
    # -> important for Mocking maybe
    
    unittest.main()

