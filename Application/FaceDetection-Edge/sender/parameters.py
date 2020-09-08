import os

""" Configurable parameters provided as enviornment variables """

remote_host = os.getenv("REMOTE_HOST","127.0.0.1")
remote_port = int(os.getenv("REMOTE_PORT","4097"))
buffer_size = int(os.getenv("BUFFER_SIZE","4096"))  # Buffer size to be send as one message
delay_bw_msgs = float(os.getenv("DELAY_BW_MSGS","0.08")) # Delay between two msgs to give receiver time to save. Larger data requires longer. 
sleep_if_nothing_to_send = float(os.getenv("SLEEP_IF_NOTHING_TO_SEND","5"))  # Sleep if no image is available to send
