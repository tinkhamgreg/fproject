FROM ubuntu:xenial

COPY . /src
WORKDIR /src
RUN chmod +x /run_test.sh"
