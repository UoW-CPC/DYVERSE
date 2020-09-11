sudo docker run \
  --name fd-pi-client \
  --device /dev/vchiq \
  -v /opt/vc:/opt/vc \
  --privileged=true \
  --env LD_LIBRARY_PATH=/opt/vc/lib \
  -e REMOTE_HOST=127.0.0.1 \
  -e REMOTE_PORT=4096 \
  -e BUFFER_SIZE=1024 \
  -e DELAY_BW_MSGS=0.08 \
  -e DELAY_BW_IMAGES=1.0 \
  uowcpc/fd-pi-client
