#!/bin/bash
DEV_NAME="PC"

SID=$(curl -s "http://192.168.54.1:60606/Server0/CMS_event" \
	-H "TIMEOUT: Second-300" -H "User-Agent: Panasonic Android/1 DM-CP"\
	-H "CALLBACK: <http://192.168.54.10:49153/Camera/event>" -H "NT: upnp:event" -v -X SUBSCRIBE 2>&1 \
	| grep "SID" | sed 's/.*://g' | strings )

echo "$SID"
curl -s "192.168.54.1/cam.cgi?mode=accctrl&type=req_acc&value=${SID}&value2=${DEV_NAME}"
curl -s "192.168.54.1/cam.cgi?mode=setsetting&type=device_name&value=${DEV_NAME}"
curl -s "192.168.54.1/cam.cgi?mode=getsetting&type=pa"
curl -s "192.168.54.1/cam.cgi?mode=camcmd&value=playmode"


# Something is still missing here, the Camera screen blackes out

exit 0
