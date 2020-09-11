docker run \
  --name fd-client \
  --device=/dev/vchiq \
  -e REMOTE_HOST=IP_ADDRESS_OF_REMOTE_HOST \
  -e REMOTE_PORT=4096 \
  -e BUFFER_SIZE=1024 \
  -e DELAY_BW_MSGS=0.08 \
  -e DELAY_BW_IMAGES=1.0 \
  uowcpc/fd-client
