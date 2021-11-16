FROM alpine:3.14.3 AS base

RUN apk add --no-cache make subversion gcc musl-dev
WORKDIR /opt/install
RUN svn checkout https://svn.code.sf.net/p/acme-crossass/code-0/trunk acme
WORKDIR /opt/install/acme/src
RUN make
RUN make install

FROM alpine:3.14.3 AS runtime

COPY --from=base /usr/local/bin/acme /bin/acme
ENTRYPOINT ["/bin/sh"]
