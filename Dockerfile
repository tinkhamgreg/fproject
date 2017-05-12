FROM ubuntu:xenial

WORKDIR /src
COPY . /src
RUN chmod +x /run_test.sh
