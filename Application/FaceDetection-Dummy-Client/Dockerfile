FROM python:3.6-slim

WORKDIR /var/lib/fd-dummy-client

COPY . .
RUN mkdir staticImages

ENV PYTHONPATH=/var/lib/fd-dummy-client

CMD ["python3","send.py"]