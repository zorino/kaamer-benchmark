FROM debian:10

ADD ghostz-1.0.2.tar.gz /opt/

RUN apt-get update; \
    apt-get install -y build-essential

RUN cd /opt/ghostz-1.0.2/; \
    make; \
    cp ghostz /usr/local/bin/; \
    chmod +x /usr/local/bin/*

RUN mkdir /data
VOLUME /data
WORKDIR /data
