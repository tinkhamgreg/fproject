FROM ubuntu:xenial

WORKDIR /src
COPY . /src
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN pip3 install Flask
RUN pip3 install prometheus_client
