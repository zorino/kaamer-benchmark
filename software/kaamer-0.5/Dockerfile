FROM golang:1.15.8-buster

# FIXUID
RUN apt-get update \
    && apt-get install -y curl \
    && curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh >> /usr/local/bin/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it.sh \
    && addgroup --gid 1000 docker \
    && adduser --uid 1000 --ingroup docker --home /home/docker --shell /bin/sh --disabled-password --gecos "" docker

RUN USER=docker && \
    GROUP=docker && \
    curl -SsL https://github.com/boxboat/fixuid/releases/download/v0.5/fixuid-0.5-linux-amd64.tar.gz | tar -C /usr/local/bin -xzf - && \
    chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid && \
    printf "user: $USER\ngroup: $GROUP\n" > /etc/fixuid/config.yml

ADD kaamer-v0.5.tar.gz /opt/

RUN cd /opt/kaamer-0.5 \
    && go install ./...

RUN mkdir /data \
    && chown docker:docker /data
VOLUME /data
WORKDIR /data

EXPOSE 8321

USER docker:docker
ENTRYPOINT ["fixuid"]
