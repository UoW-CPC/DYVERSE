# Face Detection (FD) Edge Server - Receiver
This is the Receiver component of the Edge server. It is responsible to receive video frames from a particular client.

## Tested Platform
We have tested it using Mac OS, Ubuntu and Raspberry pi.

## Requirement
- [Python](https://www.python.org/)

## How to use
### Normal run
1. Update/provide the directory, where the received images will be saved. 
2. Update the various customisable parameters in the parameters.py.
3. ```python rec.py```
### Run as docker container
1. No need to make any changes to the code. The container script will automatically create a directory. Please check the Dockerfile.
2. The customisable parameters will be provided through enviornment variables.
3. A host directory shall be mounted to the images directory of the container. The host directory will be further mounted as the input directory to the Processor component.
4. Check the scripts directory for the complete docker run command.
