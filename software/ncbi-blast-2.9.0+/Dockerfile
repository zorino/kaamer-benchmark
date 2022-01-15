FROM debian:10

# FIXUID
RUN apt-get update \
    && apt-get install -y curl \
    && addgroup --gid 1000 docker \
    && adduser --uid 1000 --ingroup docker --home /home/docker --shell /bin/sh --disabled-password --gecos "" docker

RUN USER=docker && \
    GROUP=docker && \
    curl -SsL https://github.com/boxboat/fixuid/releases/download/v0.5/fixuid-0.5-linux-amd64.tar.gz | tar -C /usr/local/bin -xzf - && \
    chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid && \
    printf "user: $USER\ngroup: $GROUP\n" > /etc/fixuid/config.yml

ADD ncbi-blast-2.9.0+-src.tar.gz /opt/

RUN apt-get update; \
    apt-get install -y build-essential cpio

RUN cd /opt/ncbi-blast-2.9.0+-src/c++/ \
    && ./configure \
    && make \
    && make install

RUN mkdir /data \
    && chown docker:docker /data
VOLUME /data
WORKDIR /data

USER docker:docker
ENTRYPOINT ["fixuid"]
