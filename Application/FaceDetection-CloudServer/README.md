# Face Detection (FD) Cloud Server
This is the Cloud server of the face detection application. Currently, it receives a customisable number of images and
temporarily stored them in a provided repository.

## Tested Platform
We have tested FD Cloud server on with Ubuntu and Mac OS.

## Requirement
- [Python](https://www.python.org/)

## How to use
1. Update various customisable aspects of the program in parameters.py. These aspects can be provided using enviornment variables, if in case running as docker container.
2. ```python cloudReceive.py```
