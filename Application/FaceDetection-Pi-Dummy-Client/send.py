"""Static images sender
Pick images one by one from a static directory of images
provided as input and send to a remote server.
"""

from socket import *
from parameters import *
import time
import logging
from os import listdir
from time import sleep

base_path = "staticImages/"
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
    logger.info("Image sent => {0}".format(fName))

def send():
    logger.info("Sleep duration => {0}".format(delay_bw_images))
    while(1):
        try:
            for file in listdir(base_path):
                file_full_name = os.path.join(base_path, file)
                if isfile(file_full_name) and file.endswith(".jpg"):
                    sendFile(file_full_name)
                    sleep(delay_bw_images)
        except Exception as err:
            logger.info("Exception occured => {0} ".format(err))
if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-pi-dummy-client."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    send()
    exit()
