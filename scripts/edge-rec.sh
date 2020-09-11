docker run \
  --name fd-edge-receiver \
  -v /path/to/images/directory/on/host:/var/lib/fd-edge-rec/images \
  -p 4096:4096/udp \
  -e PORT=4096 \
  -e BUFFER_SIZE=1024 \
  -e SOCKET_TIMEOUT=0.1 \
  uowcpc/fd-edge-receiver
