#!/usr/bin/env python

from __future__ import division
import cv2
import numpy as np
import socket
import struct
import sys
from PIL import Image
import io
import time

MAX_DGRAM = 2**16

def main():
    
    # Set up socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('192.168.54.10',49152))
    dat = b''
    
    prevtime= time.time()
    while True:
        data, addr = s.recvfrom(MAX_DGRAM)
        
        # What is inside?
        data = data[data.find(b'\xff\xd8'):]
        if data[-2:] != b'\xff\xd9':
            print('no end of jpeg found from stream')
            continue

        image = Image.open(io.BytesIO(data))
        image = np.asarray(image.resize((1440,1080)))
        

        frametime = time.time()
        fps = 1/(frametime-prevtime)
        fps = str(int(fps))
        prevtime=frametime
        cv2.putText(image, fps, (0,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
        
        cv2.imshow("frame", image)#cv2.imdecode(np.fromstring(data, dtype=np.uint8),1))
        cv2.waitKey(1)
        
        dat = b''
    
    cv2.destroyAllWindows()
    s.close()

if __name__ == "__main__":
    main()


