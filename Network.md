# Tools
- nc -l <port>
- tcpdump
- iw / ip addr
- nmap and ipscan
- wireshark
- arp
- iptables


# Setup

iptables -t nat -A PREROUTING -i anbox0 -j DNAT –to-destination 192.168.54.1
iptables -t nat -A POSTROUTING -d 192.168.54.1 -j MASQUERADE

239.255.255.250 mentioned in wireshark?

https://www.debuntu.org/how-to-redirecting-network-traffic-to-a-new-ip-using-iptables/

- when using the Image App in Anbox, Bluestacks or with a proxy, the App doesn't work since it only targets its gateway while searching for a camera.
- This behavior is correct, because the gateway is normally the camera
- Using the commands mentioned above, one should be able, to route all traffic from the Image App in Anbox to the camera
- This does work for many requests as seen in wireshark, the requests send from the image App wont get forwarded though, I guess I'm missing something.


- Some more commands for a different setup

iptables -t nat -A PREROUTING -s 10.42.0.81 -j DNAT --to-destination 192.168.54.1
iptables -t nat -A PREROUTING -s 192.168.54.1 -p tcp --dport 1111 -j DNAT --to-destination 10.42.0.81
iptables -t nat -A POSTROUTING -j MASQUERADE

# Registration

- ``curl -v http://192.168.54.1:60606/Server0/CMS_event -H "CALLBACK: <http://192.168.54.10:49153/Camera/event>" 
    -H "NT: upnp:event" -X SUBSCRIBE``

- ``curl "192.168.54.1/cam.cgi?mode=accctrl&type=req_acc&value=4D454930-0100-1000-8001-02AC0006A5E0&value2=RNE-L21"``
- ``curl "192.168.54.1/cam.cgi?mode=setsetting&type=device_name&value=RNE-L21"``
- ``curl "192.168.54.1/cam.cgi?mode=getsetting&type=pa"``
- (probably not necessary: ``curl "192.168.54.1/cam.cgi?mode=getinfo&type=capability"``)
- ( maybe ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=playmode"``)

- After registration the camera screen gets blacked out and only returnes after ca. 15 seconds
Maybe it is waiting for another command which i haven't found yet.
The Image App uses a similar timeframe for registration, so maybe it is necessary?

# Pictures

## Exposure

- ``curl "192.168.54.1/cam.cgi?mode=setsetting&type=exposure&$VALUE"``
- | $VALUE |
| --- |
| ... |

## ISO

- ``curl "192.168.54.1/cam.cgi?mode=setsetting&type=iso&value=$VALUE"``
- | $VALUE |
|---|
|100|
|200|
|400|
|800|
|1600|
|3200|
|6400|
|12800|
|256000|

## Focal length

- ``curl "192.168.54.1/cam.cgi?mode=setsetting&type=focal&value=$VALUE/256"``
- The focal length values are encoded, the values used here are retrieved by trial and error.

- |focal length | $VALUE |
|---|---|
|3.5|900|
|4.0|1000|
|4.5|1100|
|5.0|1200|
|5.6|1300|
|6.3|1400|
|7.1|1450|
|8.0|1500|
|9.0|1600|
|10|1700|
|11|1800|
|13|1900|
|14|2000|
|16|2050|
|18|2100|
|20|2200|
|22|2300|

## Shutterspeed

- ``curl "192.168.54.1/cam.cgi?mode=setsetting&type=shtrspeed&value=2390/256"``
- | shutterspeed | $VALUE |
| --- | --- |
|60|-1500|
|50|-1450|
|40|-1400|
|30|-1300|
|25|-1200|
|20|-1100|
|15|-1000|
|13|-900|
|10|-850|
|8|-800|
|6|-700|
|5|-600|
|4|-500|
|3.2|-400|
|2.5|-300|
|2|-250|
|1.6|-200|
|1.3|-100|
|1|1|
|1/1.3|100|
|1/1.6|200|
|1/2|250|
|1/2.5|300|
|1/3.2|400|
|1/4|500|
|1/5|600|
|1/6|700|
|1/8|800|
|1/10|950|
|1/13|900|
|1/15|1000|
|1/20|1100|
|1/25|1200|
|1/30|1300|
|1/50|1450|
|1/40|1400|
|1/60|1500|
|1/80|1600|
|1/100|1700|
|1/125|1800|
|1/160|1900|
|1/200|2000|
|1/250|2050|
|1/320|2100|
|1/400|2200|
|1/500|2300|
|1/640|2400|
|1/800|2500|
|1/1000|2600|
|1/1300|2650|
|1/1600|2700|
|1/2000|2800|
|1/2500|2900|
|1/3200|3000|
|1/4000|4000|

## White Balance

- ``curl "192.168.54.1/cam.cgi?mode=setsetting&type=whitebalance&value=$VALUE"``
- | $VALUE |
| --- | 
|auto|
|daylight|

## Autofocus

- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=oneshot_af"``

## Capture Image

- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=capture"``
- we need to wait for the picture -> ca. 0.5 ms + shutterspeed
- this value is mostly consistent over all shutterspeed values and probably doesn't need to be adjusted
- after that we can request a new

## Download

## get list of pictures

POST /Server0/CDS_control HTTP/1.1  
Host: 192.168.54.1:60606  
User-Agent: Panasonic Android/1 DM-CP  
Content-Type: text/xml; charset="utf-8"  
SOAPACTION: "urn:schemas-upnp-org:service:ContentDirectory:1#Browse"  
Content-Length: 751  
-> ``curl -X POST --data-binary $FILE "192.168.54.1:60606/Server0/CDS_control"``  
-> $FILE:

	<?xml version="1.0" encoding="utf-8"?>  
		<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" 
		    s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">  
		<s:Body>  
			<u:Browse xmlns:u="urn:schemas-upnp-org:service:ContentDirectory:1" 
			    xmlns:pana="urn:schemas-panasonic-com:pana">
				<ObjectID>0</ObjectID>
				<BrowseFlag>BrowseDirectChildren</BrowseFlag>
				<Filter>*</Filter>
				<StartingIndex>0</StartingIndex>
				<RequestedCount>15</RequestedCount>
				<SortCriteria></SortCriteria>
				<pana:X_FromCP>LumixLink2.0</pana:X_FromCP>
				<pana:X_RecGroupType></pana:X_RecGroupType>
				<pana:X_Filter>type=date,value=relative,value2=0</pana:X_Filter>
				<pana:X_Order>type=date,value=descend</pana:X_Order>
			</u:Browse>
		</s:Body>
	</s:Envelope>

- StartingIndex und RequestedCount interesting, selects the pictures
- the three <pana:...> Elements are maybe not necessary?

## Download picture by name

- ``curl "192.168.54.1:60606/D01020394.jpg"``
- with this example, one could download the picture D01020394.jpg
- it doesn't work like that yet, nothing gets downloaded, maybe another command is missing beforehand?

# Streaming

- ``curl "192.168.54.1/cam.cgi?mode=startstream&value=49152"`` , -> start streaming to/from Port 49152
- Data gets send from 192.168.54.1:65415 to 192.168.54.10:49152 via UDP
- encoding / format unknown
- ffprobe does not return anything / nothing is picked up

# Unknown

- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=playmode"``, Some setting i guess?
- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=recmode"``, --""--, in combination with prev command.  
( Maybe for Streaming?)

- ``curl "192.168.54.1/cam.cgi?mode=camctrl&type=asst_disp&value=current_auto&value2=mf_asst/0/0"``, ??
- ``curl "192.168.54.1/cam.cgi?mode=camctrl&type=focus&value=wide-normal"``, ?? Some Lense settings?
- ``curl "192.168.54.1/cam.cgi?mode=camctrl&type=focus&value=tele-normal"``, --""-- exchanges with previous command
- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=autoreviewunlock"``, ??

- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=menu_entry"``, used for opening the menu for iso and shutterspeed in the app, probably not important?
- ``curl "192.168.54.1/cam.cgi?mode=camcmd&value=menu_exit"``, used for closing the menu again
- ``curl "192.168.54.1/cam.cgi?mode=getinfo&type=capability"``, returns large document, maybe interesting?
