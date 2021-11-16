FROM alpine:3.14.3 AS base

ARG REVISION
ARG REPO

RUN apk add --no-cache make subversion gcc musl-dev
WORKDIR /opt/install
RUN svn checkout -r $REVISION $REPO acme
WORKDIR /opt/install/acme/src
RUN make
RUN make install

FROM alpine:3.14.3 AS runtime

COPY --from=base /usr/local/bin/acme /bin/acme
ENTRYPOINT ["/bin/sh"]
