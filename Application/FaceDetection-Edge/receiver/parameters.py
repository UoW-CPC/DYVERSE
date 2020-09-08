import os

""" Configurable parameters provided as enviornment variables """

port = int(os.getenv("PORT","4096"))
buffer_size = int(os.getenv("BUFFER_SIZE","4096"))  # Buffer size to be send as one message
socket_timeout = float(os.getenv("SOCKET_TIMEOUT","0.1")) # Timeout before close connection for current msg