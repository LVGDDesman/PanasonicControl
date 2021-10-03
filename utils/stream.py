import sys
import cv2
import numpy as np
from PIL import Image
import io
import time

# open frame files
for file in range(600,700):
    data = b''
    with open("./frames/frame0"+str(file), "rb") as frame:
        data = frame.read()

    # What is inside?
    data = data[data.find(b'\xff\xd8'):]
    if data[-2:] != b'\xff\xd9':
        print('no end of jpeg found from stream')
    image = Image.open(io.BytesIO(data))
    cv2.imshow("frame", np.asarray(image))
    cv2.waitKey(80)
    #cv2.destroyAllWindows()

