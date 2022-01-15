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

ADD diamond-linux64.tar.gz /usr/local/bin/

RUN chmod +x /usr/local/bin/*

RUN mkdir /data \
    && chown docker:docker /data
VOLUME /data
WORKDIR /data

USER docker:docker
ENTRYPOINT ["fixuid"]
