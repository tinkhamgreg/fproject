FROM ubuntu:xenial

COPY . /src
RUN chmod +x docker-entrypoint.sh
WORKDIR /src

