FROM ubuntu:xenial

WORKDIR /src

RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN pip3 install Flask
COPY . /src
EXPOSE 8080
EXPOSE 8081
