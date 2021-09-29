#!/usr/bin/env python

from __future__ import division
import cv2
import numpy as np
import socket
import struct

MAX_DGRAM = 2**16

def dump_buffer(s):
    """ Emptying buffer frame """
    while True:
        seg, addr = s.recvfrom(MAX_DGRAM)
        print(seg[0])
        if struct.unpack("B", seg[0:1])[0] == 1:
            print("finish emptying buffer")
            break

def main():
    """ Getting image udp frame &
    concate before decode and output image """
    
    # Set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW socket.SOCK_DGRAM)
    s.bind(('192.168.54.10',49152))
    dat = b''
    #dump_buffer(s)
    i = 0
    while True:
        dat, addr = s.recvfrom(MAX_DGRAM)
        #dat = seg[1:]
        img = cv2.imdecode(np.fromstring(dat, dtype=np.uint8), 1)
        #cv2.imshow('frame', img)
        if not cv2.imwrite("./frames/coolframe"+str(i)+".jpg", img):
            print("not saved")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        dat = b''
        i+=1
    # cap.release()
    cv2.destroyAllWindows()
    s.close()

if __name__ == "__main__":
    main()
