FROM python:3.6-slim

WORKDIR /var/lib/fd-edge-send

COPY . .

RUN mkdir greyImages

ENV PYTHONPATH=/var/lib/fd-edge-send

ENTRYPOINT python3 edgeSend.py