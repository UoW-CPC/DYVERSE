FROM python:3.6-slim
WORKDIR /var/lib/fd-edge-pro

COPY . .

RUN pip3 install -r requirements.txt \
&& rm requirements.txt

RUN mkdir images
RUN mkdir greyImages

ENV PYTHONPATH=/var/lib/fd-edge-pro

ENTRYPOINT python3 2grey.py
