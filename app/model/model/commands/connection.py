#!/usr/bin/env python3
"""
Storage for all connection information
Singleton
Maybe store Information for each camera in a Database? -> Shouldn't change anyway...
"""

class Connection():

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
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, client_ip = None, server_ip = None, upnp_port = None, download_port = None, 
            stream_port = None, http_port = None, uuid = None, server_name = None, client_name = None):
        if cls._instance is None:
            print('Creating new instance')
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

    def initialize_g81_dmc():
    '''
    Initialize object for the camera G81 DMC
    -> a more general approach is useful
    '''
        client_ip = "192.168.54.1"
        server_ip = "192.168.54.10"
        upnp_port = 60606
        download_port = 50001
        stream_port = 49152
        http_port = 80
        uuid = "4D454930-0100-1000-8000-1848CA69497D"
        server_name = "G81-69497D"
        client_name = "DMC-Control"

    def get_client_ip():
        return self.client_ip

    def set_client_ip(client_ip):
        self.client_ip = client_ip

    def get_server_ip():
        return self.server_ip

    def set_server_ip(server_ip):
        self.server_ip = server_ip
    
    def get_upnp_port():
        return self.upnp_port

    def set_upnp_port(upnp_port):
        self.upnp_port = upnp_port

    def get_download_port():
        return self.download_port

    def set_download_port(download_port):
        self.download_port = download_port

    def get_stream_port():
        return self.stream_port

    def set_stream_port(stream_port):
        self.stream_port = stream_port

    def get_http_port():
        return self.http_port

    def set_http_port(http_port):
        self.http_port = http_port

    def get_uuid():
        return self.uuid

    def set_uuid(uuid):
        self.uuid = uuid

    def get_server_name():
        return self.server_name

    def set_server_name(server_name):
        self.server_name = server_name

    def get_client_name():
        return self.client_name

    def set_client_name(client_name):
        self.client_name = client_name
