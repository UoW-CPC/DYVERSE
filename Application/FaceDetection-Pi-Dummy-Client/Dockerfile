FROM resin/raspberry-pi-python:3.6-slim

WORKDIR /var/lib/fd-pi-dummy-client

COPY . .
RUN mkdir staticImages

ENV PYTHONPATH=/var/lib/fd-pi-dummy-client

#ENTRYPOINT python3 /var/lib/fd-pi-client/captureSend.py
#RUN echo "$PWD"
CMD ["python3","send.py"]