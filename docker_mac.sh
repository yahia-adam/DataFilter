# Build the image
docker build -t datafilter .

# # Get IP address of Mac
IP=$(/usr/sbin/ipconfig getifaddr en0)

# # Print IP address
echo "IP: $IP"

# # Allow connections through XQuartz
/opt/X11/bin/xhost + "$IP"

# Run the container
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$IP:0 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm -it datafilter