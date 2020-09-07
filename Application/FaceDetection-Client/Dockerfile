FROM python:3.6-slim
WORKDIR /var/lib/fd-client

COPY . .

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN pip3 install -r requirements.txt \
&& rm requirements.txt

ENV PYTHONPATH=/var/lib/fd-client

ENTRYPOINT python3 captureSend.py