# Face Detection (FD) Client
This is the webcam video streaming client of the face detection application. It captures frames in real time and send them to the remote server for analysis.

## Tested Platform
We have tested FD Client with macOS and Ubuntu.

## Requirement
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)

## How to use
1. Update the various parameters of the program in parameters.py. These can be provided using enviornment variables, if in case running as docker container.
2. ```python captureSend.py```
