import unittest
from unittest import mock

import os
import sys
from mock_service import *

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Modules to test
import controller.commands as commands
from model.structures.connection import Connection

class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_g81_dmc_test(Connection())


    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_upnp_client(self, mock_get):
        # NOT WORKING
        #upnp_client = Upnp_client()
        #response = upnp_client.
        #self.assertEqual(response.successful, True)
        return

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_capture(self, mock_get):
        response = commands.Capture.execute()
        self.assertEqual(True, response.successful)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_start_stream(self, mock_get):
        response = commands.Start_stream.execute()

        self.assertEqual(response.successful, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_stop_stream(self, mock_get):
        response = commands.Stop_stream.execute()

        self.assertEqual(response.successful, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_downloader(self, mock_get):
        response = commands.Downloader.execute(picture="TEST.jpg", folder=".output/")
        self.assertEqual(response.successful, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_picture_list(self, mock_get):
        commands.Upnp_client().initiate_registration()
        response = commands.Get_picture_list.execute(count=20)

        self.assertEqual(response.successful, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_setting(self, mock_get):
        response = commands.Get_setting.execute(setting_type="shtrspeed")

        self.assertEqual(response.successful, True)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_registration(self, mock_get):
        response = commands.Registration.execute()
        self.assertEqual(response.successful, True)
        return

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_set_setting(self, mock_get):
        response = commands.Set_setting.execute(setting_type="shtrspeed", setting_value="2390/256")

        self.assertEqual(response.successful, True)


if __name__ == "__main__":
    unittest.main()
