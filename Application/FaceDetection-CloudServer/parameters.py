import os

""" Configurable parameters provided as enviornment variables """

port = int(os.getenv("PORT","4097"))
buffer_size = int(os.getenv("BUFFER_SIZE","500"))  # Buffer size to be send as one message
socket_timeout = float(os.getenv("SOCKET_TIMEOUT","0.1")) # Timeout before close connection for current msg
max_no_of_images = int(os.getenv("MAX_NO_OF_IMAGES","100"))  # Max limit for the number of images to be kept