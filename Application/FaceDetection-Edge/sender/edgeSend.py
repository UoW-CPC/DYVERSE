"""Edge sender
This program sends images, using socket,
from a directory to a remote address.
"""

from socket import *
from parameters import *
import time
import logging
from os import listdir
from os.path import isfile, join
from time import sleep

addr = (remote_host, remote_port)
#base_path = "/Users/ullaha/Dropbox/office/fog-micado/FaceDetection/Version2/edge/vol/greyImages/"
base_path = "greyImages/"

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

def get_file():
    for file in listdir(base_path):
        file_full_name = os.path.join(base_path, file)
        if isfile(file_full_name) and file.endswith(".jpg") and file.startswith("tmp_") == False:
            file_name = os.path.join(base_path, file)
            return file_name
    return ""

def handle_send():
    logger.info("Edge sender component running..")
    logger.info("Delay bw msgs => {0}".format(delay_bw_msgs))
    logger.info("Remote address => {0}:{1}".format(remote_host,remote_port))
    while True:
        try:
            file_name = get_file()
            if file_name != "":
                logger.info ("Sending file => {0}".format(file_name))
                sendFile(file_name)
                os.remove(file_name)
                time.sleep(1)
            else:
                logger.info("No image to send, sleeping for => {0} seconds".format(sleep_if_nothing_to_send))
                time.sleep(sleep_if_nothing_to_send)
        except Exception as err:
            logger.info("Exception during send => {0} ".format(err))        
if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-edge-sender."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    handle_send()
