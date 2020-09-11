docker run \
  --name fd-cloud \
  -v /path/to/images/directory/on/host:/var/lib/fd-cloud/images \
  -p 4097:4097/udp \
  -e PORT=4097 \
  -e BUFFER_SIZE=1024 \
  -e SOCKET_TIMEOUT=0.1 \
  -e MAX_NO_OF_IMAGES=100 \
uowcpc/fd-cloud
