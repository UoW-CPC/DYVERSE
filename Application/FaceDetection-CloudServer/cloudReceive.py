""" Cloud component
This program act as the component that has to run on the centralised
cloud environment. Currently, it receives a customisable number of images and
temporarily stored them in a provided repository. This component
can be further extended for any excessive computational task.
"""

from socket import *
from time import time
from parameters import *
import logging
import uuid

host = "0.0.0.0"  # To use public IP
addr = (host, port)
base_path = 'images/'
img_current_index = 0
list_file_names = []
def generate_image_name():
    file_name = str(uuid.uuid4()) + ".jpg"
    return file_name

def handle():
    logger.info("Cloud component running...")
    logger.info("Listening port => {0}".format(port))
    logger.info("Socker timeout=> {0}".format(socket_timeout))
    img_current_index=0
    while True:
        try:
            s = socket(AF_INET, SOCK_DGRAM)
            s.bind(addr)
            gen_file_name = generate_image_name()
            file_name = base_path + gen_file_name
            f = open(file_name, 'wb')
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
            fileSize = os.path.getsize(file_name)
            logger.info("Address => {0} , Field Size => {1}".format(address, fileSize))
            #  Dealt with images
            if len(list_file_names) >= max_no_of_images:
                file_name_to_be_deleted = list_file_names[0]
                full_path = base_path + file_name_to_be_deleted
                os.remove(full_path)
                list_file_names.insert(max_no_of_images-1,file_name)
            else:
                list_file_names.insert(img_current_index,file_name)
                img_current_index = img_current_index + 1    
        except Exception as exc:
            logger.info("Exception occured => {0}".format(exc))
        
if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-cloud."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    handle()