FROM python:3.6-slim
WORKDIR /var/lib/fd-edge-rec

COPY . .


RUN mkdir images

ENV PYTHONPATH=/var/lib/fd-edge-rec

ENTRYPOINT python3 rec.py
