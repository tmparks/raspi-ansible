FROM alpine:latest

RUN apk add --no-cache \
    ansible \
    git
