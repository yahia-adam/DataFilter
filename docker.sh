#!/bin/bash

# Build the image
docker build -t flaskapp .

# Get IP address of the host
IP=$(hostname -I | awk '{print $1}')

# Print IP address
echo "IP: $IP"

# Allow connections to X server
xhost +local:docker

# Run the container
docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
           -v $HOME/.Xauthority:/root/.Xauthority:rw \
           --net=host \
           --rm -it flaskapp