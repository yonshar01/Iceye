#### Use latest Ubuntu
FROM ubuntu:18.04

# Update base container install
RUN apt-get -y update;  apt-get -y install curl

#
## Create the root directory to store the scripts
RUN mkdir -p /home/larvis

# binary to the container
ADD /files/larvis /home/larvis/

# working directory
WORKDIR /home/larvis










