#!/usr/bin/env python3

from model.design_pattern.singleton import Singleton

class Connection(metaclass = Singleton):
    """
    Storage for all connection information
    """
    def __init__(self):
        self._client_ip = None 
        self._server_ip = None
        self._upnp_port = None
        self._download_port = None
        self._stream_port = None
        self._http_port = None 
        self._uuid = None 
        self._server_name = None 
        self._client_name = None 

    def initialize_g81_dmc(self):
        """
        Initialize object for the camera G81 DMC
        -> a more general approach is useful
        """
        self._client_ip = "192.168.54.10"
        self._server_ip = "192.168.54.1"
        self._upnp_port = 60606
        self._download_port = 50001
        self._stream_port = 49152
        self._http_port = 80
        self._uuid = "4D454930-0100-1000-8000-1848CA69497D"
        self._server_name = "G81-69497D"
        self._client_name = "DMC-Control"
    
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        self._client_ip = client_ip
    
    @property
    def server_ip(self):
        return self._server_ip
    
    @server_ip.setter
    def server_ip(self, server_ip):
        self._server_ip = server_ip
    
    @property 
    def upnp_port(self):
        return self._upnp_port
    
    @upnp_port.setter
    def upnp_port(self, upnp_port):
        self._upnp_port = upnp_port
    
    @property
    def download_port(self):
        return self._download_port

    @download_port.setter
    def download_port(self, download_port):
        self._download_port = download_port

    @property
    def stream_port(self):
        return self._stream_port
    
    @stream_port.setter
    def stream_port(self, stream_port):
        self._stream_port = stream_port

    @property
    def http_port(self):
        return self._http_port
    
    @http_port.setter 
    def http_port(self, http_port):
        self._http_port = http_port

    @property
    def uuid(self):
        return self._uuid
    
    @uuid.setter 
    def uuid(self, uuid):
        self._uuid = uuid

    @property
    def server_name(self):
        return self._server_name
    
    @server_name.setter
    def server_name(self, server_name):
        self._server_name = server_name

    @property
    def client_name(self):
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        self._client_name = client_name
