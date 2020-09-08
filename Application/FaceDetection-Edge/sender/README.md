# Face Detection (FD) Edge Server - Sender
This is the Sender component of the Edge server. It is responsible for sending the grey images to a remote server.

## Tested Platform
We have tested it using Mac OS, Ubuntu and Raspberry pi.

## Requirement
- [Python](https://www.python.org/)

## How to use
### Normal run
1. Update/provide the directory, where the grey images will be picked for sending. 
2. Update the various customisable parameters in the parameters.py.
3. ```python edgeSend.py```
### Run as docker container
1. No need to make any changes to the code. The container script will automatically create a directory. Please check the Dockerfile.
2. The customisable parameters will be provided through enviornment variables.
3. A host directory shall be mounted to the images directory of the container.
4. Check the scripts directory for the complete docker run command.
