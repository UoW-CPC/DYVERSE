"""Webcam video streaming
Using OpenCV to capture frames from webcam.
Compress each frame to jpeg and save it.
Using socket to read from the jpg and send
it to remote address.
"""

import cv2
from socket import *
from parameters import *
import time
import logging

cap = cv2.VideoCapture(0)

FPS = cap.get(5)
ratio = int(FPS)/frame_per_second

addr = (remote_host, remote_port)

def sendFile(fName):
    s = socket(AF_INET, SOCK_DGRAM)
    #s.sendto(fName, addr)
    f = open(fName, "rb")
    data = f.read(buffer_size)
    while data:
       if(s.sendto(data, addr)):
           data = f.read(buffer_size)
           time.sleep(delay_bw_msgs) # Give receiver time to save. Larger data requires longer.
    f.close()
    s.close()
    logger.info("Image sent.")

def captureFunc():
    count = 0
    logger.info("FPS=> {0}".format(frame_per_second))
    logger.info("Sleep duration bw two images => {0}".format(delay_bw_images))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            count = count + 1
            if count == ratio:
                logger.info ("Start time=> {0}".format(time.time()))
                cv2.imwrite("img.jpg", frame)
                sendFile("img.jpg")
                count = 0
                time.sleep(delay_bw_images)
                #break

if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-client."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    captureFunc()
    cap.release()
