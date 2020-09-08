""" Edge pre-processor component
This program, expected to run on a Fog/Edge node. Currently, it perform
the following functions:
1) Detect face in an image,
2) If found, convert the image to a grey image
3) stores them in a specified directory to be send to a remote machine.
"""

from socket import *
from PIL import Image
import os
import time
from parameters import *
import logging
from PIL import ImageFile
from os import listdir
import cv2
from os.path import isfile, join
ImageFile.LOAD_TRUNCATED_IMAGES = True

in_base_path = "images/"
out_base_path ="greyImages/"

def get_file():
    for file in listdir(in_base_path):
        file_full_name = os.path.join(in_base_path, file)
        if isfile(file_full_name) and file.endswith(".jpg") and file.startswith("tmp_") == False:
            tmp_file_name = os.path.join(in_base_path, "tmp_"+ file)
            os.rename(file_full_name,tmp_file_name)
            return tmp_file_name, file
    return "", ""

def handle():
    logger.info("Edge processor is running...")
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    while True:
        try:
            tmp_file_name, file_name = get_file()
            #logger.info("tmp_file_name => {0} \n file_name => {1}".format(tmp_file_name,file_name))
            if tmp_file_name == "":
                logger.info("No image to process")
                time.sleep(sleep_period)
                continue
            start_time = time.time()
            logger.info("Analysis start time => {0}".format(start_time))

            # Face detection
            logger.info ("Detecting face...")
            image = cv2.imread(tmp_file_name)
            faces = faceCascade.detectMultiScale(
                                             image,
                                             scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(30, 30)
                                             )
            if len(faces) > 0:
                logger.info ("Faces => {0}".format(faces))
                # Greyscale
                grayImg = Image.open(tmp_file_name).convert('L')
                output_file = os.path.join(out_base_path, file_name)
                grayImg.save(output_file)
                # record file sizes
                in_fileSize = os.path.getsize(tmp_file_name)
                out_fileSize = os.path.getsize(output_file)
                logger.info("Input file size => {0} \nGrey file size => {1}".format(in_fileSize, out_fileSize))
            # Delete file
            os.remove(tmp_file_name)
            logger.info("Analysis duration => {0}".format(time.time() - start_time))
        except Exception as err:
            logger.info("Exception occured => {0} ".format(err))
if __name__ == '__main__':
    global logger
    logger =  logging.getLogger("fd-edge."+__name__)
    logging.basicConfig(level=logging.DEBUG)
    handle()

