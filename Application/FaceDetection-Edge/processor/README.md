# Face Detection (FD) Edge Server - Processor
This is the Edge server of FD, which detect faces in the video frames and converts into grayscale scale.

## Tested Platform
We have tested it using Mac OS, Ubuntu and Raspberry pi.

## Requirement
- [Python](https://www.python.org/),
- [OpenCV](https://opencv.org/),
- [image] (https://pypi.org/project/image/)

## How to use
### Normal run
1. Update/provide the input images directory and output images directory the 2grey.py. 
2. Specify the sleep duration for the program for scenario, when no input image is available to process.
3. ```python 2grey.py```
### Run as docker container
1. No need to make any changes to the code. The container script will automatically create input and out directories. Please check the Dockerfile.
2. The sleep duration must be specified through enviornment variable.
3. Check the scripts directory for the complete docker run command.
