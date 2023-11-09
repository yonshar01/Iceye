#### Use latest Ubuntu
FROM ubuntu

# Update base container install
RUN apt-get update
RUN apt-get curl

#
## Create the root directory to store the scripts
RUN mkdir -p /home/Larvis/files

COPY files/larvis /home/Larvis/files/

WORKDIR /home/larvis










