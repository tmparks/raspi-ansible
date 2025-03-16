# Development container for ansible
FROM alpine

RUN apk add --no-cache \
    ansible \
    git \
    openssh-client

RUN adduser --disabled-password user
USER user
WORKDIR /home/user
