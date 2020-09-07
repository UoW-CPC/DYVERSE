FROM python:3.6-slim
WORKDIR /var/lib/fd-cloud

COPY . .

RUN mkdir images

ENV PYTHONPATH=/var/lib/fd-cloud

ENTRYPOINT python3 cloudReceive.py