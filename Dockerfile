# Development container for ansible
FROM alpine

RUN apk add --no-cache \
    ansible \
    git \
    openssh-client \
    rsync

RUN adduser --disabled-password user
USER user
WORKDIR /home/user
