#!/usr/bin/env python3

class Connection():
    """
    Storage for all connection information
    Singleton
    """

    _instance = None

    # dynamic information:
    client_ip = None
    server_ip = None
    upnp_port = None
    # Set by UPNP (probably)
    uuid = None
    server_name = None
    # infomration retrived through camera model:
    download_port = None
    stream_port = None
    http_port = None
    client_name = None

    def __init__(self):
        raise RuntimeError('Call instance(self) instead')

    @classmethod
    def instance(cls, client_ip = None, server_ip = None, upnp_port = None, download_port = None, 
            stream_port = None, http_port = None, uuid = None, server_name = None, client_name = None):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.client_ip = client_ip
            cls.server_ip = server_ip
            cls.upnp_port = upnp_port
            cls.download_port = download_port
            cls.stream_port = stream_port
            cls.http_port = http_port
            cls.uuid = uuid
            cls.server_name = server_name
            cls.client_name = client_name
        return cls._instance

    def initialize_g81_dmc(self):
        '''
        Initialize object for the camera G81 DMC
        -> a more general approach is useful
        '''
        self.client_ip = "192.168.54.10"
        self.server_ip = "192.168.54.1"
        self.upnp_port = 60606
        self.download_port = 50001
        self.stream_port = 49152
        self.http_port = 80
        self.uuid = "4D454930-0100-1000-8000-1848CA69497D"
        self.server_name = "G81-69497D"
        self.client_name = "DMC-Control"

    def get_client_ip(self):
        return self.client_ip

    def set_client_ip(self, client_ip):
        self.client_ip = client_ip

    def get_server_ip(self):
        return self.server_ip

    def set_server_ip(self, server_ip):
        self.server_ip = server_ip
    
    def get_upnp_port(self):
        return self.upnp_port

    def set_upnp_port(self, upnp_port):
        self.upnp_port = upnp_port

    def get_download_port(self):
        return self.download_port

    def set_download_port(self, download_port):
        self.download_port = download_port

    def get_stream_port(self):
        return self.stream_port

    def set_stream_port(self, stream_port):
        self.stream_port = stream_port

    def get_http_port(self):
        return self.http_port

    def set_http_port(self, http_port):
        self.http_port = http_port

    def get_uuid(self):
        return self.uuid

    def set_uuid(self, uuid):
        self.uuid = uuid

    def get_server_name(self):
        return self.server_name

    def set_server_name(self, server_name):
        self.server_name = server_name

    def get_client_name(self):
        return self.client_name

    def set_client_name(self, client_name):
        self.client_name = client_name
