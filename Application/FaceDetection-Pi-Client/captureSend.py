"""Webcam video streaming
Using OpenCV to capture frames from webcam.
Compress each frame to jpeg and save it.
Using socket to read from the jpg and send
it to remote address.
"""

from socket import *
from parameters import *
import time
import logging
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = frame_per_second

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
    logger.info("FPS=> {0}".format(frame_per_second))
    logger.info("Sleep duration => {0}".format(delay_bw_images))
    logger.info("Frame rate => {0}".format(camera.framerate))
    while(1):
        #camera.start_preview()
        logger.info ("Start time=> {0}".format(time.time()))
        camera.capture('images/img.jpg', quality=10)
        sendFile("images/img.jpg")
        sleep(delay_bw_images)
        
if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-pi-client."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    captureFunc()
    camera.close()
    exit()
