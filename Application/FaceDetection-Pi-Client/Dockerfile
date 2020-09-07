FROM arm32v7/python:3.6-buster

WORKDIR /var/lib/fd-pi-client

COPY . .

RUN pip install -r requirements.txt \
&& rm requirements.txt

ENV PYTHONPATH=/var/lib/fd-pi-client

ENTRYPOINT python3 captureSend.py