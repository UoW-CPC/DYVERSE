FROM python:3.6-slim
WORKDIR /var/lib/fd-edge

COPY . .


RUN mkdir images

ENV PYTHONPATH=/var/lib/fd-edge

ENTRYPOINT python3 rec.py
