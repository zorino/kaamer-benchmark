FROM debian:10

ADD ncbi-blast-2.9.0+-x64-linux.tar.gz /opt/

RUN cp /opt/ncbi-blast-2.9.0+/bin/* /usr/local/bin/

RUN mkdir /data
VOLUME /data
WORKDIR /data
