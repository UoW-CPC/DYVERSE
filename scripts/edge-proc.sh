docker run \
  --name fd-edge-processor \
  -v /path/to/images/directory/on/host:/var/lib/fd-edge-pro/images \
  -v /path/to/greyImages/directory/on/host:/var/lib/fd-edge-pro/greyImages \
  -e SLEEP_PERIOD=2 \
  uowcpc/fd-edge-processor
