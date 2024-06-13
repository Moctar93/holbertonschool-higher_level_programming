FROM alpine:latest

RUN apk add --no-cache curl

COPY hello.txt /app/hello.txt

VOLUME /data

CMD ["echo", "Hello, World!"]
