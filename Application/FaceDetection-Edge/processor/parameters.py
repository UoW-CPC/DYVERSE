import os

""" Configurable parameters provided as enviornment variables """

sleep_period = float(os.getenv("SLEEP_PERIOD","2")) # Sleep duration when no image to process
