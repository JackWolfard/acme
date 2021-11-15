FROM alpine:3.14.3 AS base

RUN apk add --no-cache make git gcc musl-dev
WORKDIR /opt/install
RUN git clone https://github.com/meonwax/acme.git
WORKDIR /opt/install/acme/src
RUN make
RUN make install

FROM alpine:3.14.3 AS runtime

COPY --from=base /usr/local/bin/acme /bin/acme
ENTRYPOINT ["/bin/sh"]
