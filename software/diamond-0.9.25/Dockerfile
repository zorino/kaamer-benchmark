FROM debian:10

ADD diamond-linux64.tar.gz /usr/local/bin/

RUN chmod +x /usr/local/bin/*

RUN mkdir /data
VOLUME /data
WORKDIR /data
