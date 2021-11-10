client_ip = "192.168.54.10"
server_ip = "192.168.54.1"
upnp_port = 60606
download_port = 50001
stream_port = 49152
http_port = 80
uuid = ""
server_name = "G81-69497D"
client_name = "DMC-Control"

def initialize_g81_dmc_test(connection):
    """
    Initialize object for the camera G81 DMC
    -> a more general approach is useful
    """
    connection.client_ip = client_ip
    connection.server_ip = server_ip
    connection.upnp_port = upnp_port
    connection.download_port = download_port
    connection.stream_port = stream_port
    connection.http_port = http_port
    connection.uuid = uuid
    connection.server_name = server_name
    connection.client_name = client_name
        
def mocked_requests_get( *args, **kwargs):

    getsetting = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" \
                 "<camrply><result>ok</result><settingvalue {}=\"{}\"></settingvalue></camrply>"

    class MockResponse:
        def __init__(self, text="", status_code=404, content=""):
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
    if args[0] == 'http://192.168.54.1:80/cam.cgi?mode=startstream&value=' + str(stream_port):
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)
    # Stop Stream 
    if args[0] == 'http://192.168.54.1:80/cam.cgi?mode=stopstream':
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)
    ## set Settings
    elif 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=shtrspeed&value=' in args[0] \
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=iso&value=' in args[0] \
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=focal&value=' in args[0] \
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=exposure&value=' in args[0] \
            or 'http://192.168.54.1:80/cam.cgi?mode=setsetting&type=whitebalance&value=' in args[0]:
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)

    ## Autofocus
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=camcmd&value=oneshot_a':
        return MockResponse("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<camrply><result>ok</result></camrply>", 200)

    ## get Picturelist
    elif args[0] == 'http://192.168.54.1:60606/Server0/CDS_control':
        with open("answers/picturelist.xml", "r") as file:
            return MockResponse(file.read(), 200)

    ## Download pictures

    elif args[0] == 'http://192.168.54.1:50001/TEST.jpg':
        with open("answers/TEST.jpg", "rb") as file:
            return MockResponse(status_code=200, content=file.read())

    # WIP:
    elif args[0] == 'http://192.168.54.1:60606/Server0/CMS_event':
        return MockResponse(uuid, 200)

    elif args[0] == 'http://192.168.54.1/cam.cgi?mode=accctrl&type=req_acc&value=' + uuid + '&value2=RNEL21':
        return MockResponse("", 200)

    ## get Settings
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=shtrspeed':
        return MockResponse(getsetting.format("shtrspeed", "2390/256"), 200)
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=iso':
        return MockResponse(getsetting.format("iso", "800"), 200)
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=focal':
        return MockResponse(getsetting.format("focal", "925/256"), 200)
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=exposure':
        return MockResponse(getsetting.format("shtrspeed", "1"), 200)  # NOT RIGHT
    elif args[0] == 'http://192.168.54.1:80/cam.cgi?mode=getsetting&type=whitebalance':
        return MockResponse(getsetting.format("whitebalane", "auto"), 200)
    
    print("ERROR unknown request URL: " + args[0])
    return MockResponse("", 404)
