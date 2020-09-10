# FROM alpine AS builder
# # Download QEMU, see https://github.com/docker/hub-feedback/issues/1261
# ENV QEMU_URL https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz
# RUN apk add curl && curl -L ${QEMU_URL} | tar zxvf - -C . --strip-components 1

# #FROM arm32v7/python:3.6-buster
# FROM balenalib/raspberrypi3-debian-python:latest
# # Add QEMU
# COPY --from=builder qemu-arm-static /usr/bin
# WORKDIR /var/lib/fd-pi-client
# COPY . .

# RUN READTHEDOCS=True pip install picamera
# #RUN pip install -r requirements.txt \
# && rm requirements.txt
# ENV PYTHONPATH=/var/lib/fd-pi-client
# ENTRYPOINT python3 captureSend.py


FROM resin/raspberry-pi-python:3

WORKDIR /var/lib/fd-pi-client

COPY . .

RUN READTHEDOCS=True pip install picamera

ENV PYTHONPATH=/var/lib/fd-pi-client

#ENTRYPOINT python3 /var/lib/fd-pi-client/captureSend.py
CMD ["python3","captureSend.py"]