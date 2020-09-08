""" Edge receiver component
This program, expected to run on a Fog/Edge node  
receive images from a Client instance.
"""
from socket import *
import os
from time import time
from parameters import *
import logging
import uuid

host = "0.0.0.0"
addr = (host, port)
base_path = 'images/'

def generate_image_name():
    file_name = str(uuid.uuid4()) + ".jpg"
    return file_name

def handle():
    logger.info("Edge image receive component running...")
    while True:
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(addr)

        gen_file_name = generate_image_name()
        tmp_file_name = base_path + "tmp_" + gen_file_name
        file_name = base_path + gen_file_name 

        f = open(tmp_file_name, 'wb')

        data, address = s.recvfrom(buffer_size)
        logger.info("Read start => {0}".format(time()))
        try:
            while(data):
                f.write(data)
                s.settimeout(socket_timeout)
                data, address = s.recvfrom(buffer_size)
        except timeout as err:
            logger.info("Timeout => {0} ".format(err))
            f.close()
            s.close()
        logger.info("Read finish => {0}".format(time()))
        fileSize = os.path.getsize(tmp_file_name)
        logger.info("Address => {0} , Field Size => {1}".format(address, fileSize))
        # Rename the tmp file
        os.rename(tmp_file_name,file_name)

if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-edge-receive."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    handle()

