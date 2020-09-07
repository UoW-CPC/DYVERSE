# Face Detection (FD) pi-Client
This is the webcam video streaming client of the face detection application for Raspberry pi. It captures frames in real time and send them to the remote server for analysis.

## Tested Platform
We have tested this program on Raspberry pi.

## Requirement
- [Python](https://www.python.org/)
- [Picamera](https://picamera.readthedocs.io/en/release-1.13/)

## How to use
1. Update the various parameters of the program in parameters.py. These can be provided using enviornment variables, if in case running as docker container.
2. ```python captureSend.py```
