docker run \
  --name fd-edge-sender \
  -v /path/to/greyImages/directory/on/host:/var/lib/fd-edge-send/greyImages \
  -e REMOTE_HOST=127.0.0.1 \
  -e REMOTE_PORT=4097 \
  -e BUFFER_SIZE=1024 \
  -e DELAY_BW_MSGS=0.08 \
  -e SLEEP_IF_NOTHING_TO_SEND=2 \
  uowcpc/fd-edge-sender
