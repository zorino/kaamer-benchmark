FROM debian:10

ADD ncbi-blast-2.9.0+-src.tar.gz /opt/

RUN apt-get update; \
    apt-get install -y build-essential cpio

RUN cd /opt/ncbi-blast-2.9.0+-src/c++/ \
    && ./configure \
    && make \
    && make install

RUN mkdir /data
VOLUME /data
WORKDIR /data
