import os

""" Configurable parameters provided as enviornment variables """

remote_host = os.getenv("REMOTE_HOST","127.0.0.1")
remote_port = int(os.getenv("REMOTE_PORT","4096"))
frame_per_second = int(os.getenv("FRAME_PER_SECOND","30"))  # Change this for load testing
buffer_size = int(os.getenv("BUFFER_SIZE","4096"))  # Buffer size to be send as one message
delay_bw_msgs = float(os.getenv("DELAY_BW_MSGS","0.08")) # Delay between two msgs to give receiver time to save. Larger data requires longer. 
delay_bw_images = float(os.getenv("DELAY_BW_IMAGES","0.0")) # Delay between two image captures.

