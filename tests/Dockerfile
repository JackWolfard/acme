ARG TAG=latest

FROM jackwolfard/acme:$TAG AS base

ARG REVISION
ARG REPO

RUN apk add --no-cache subversion
WORKDIR /opt
RUN svn checkout -r $REVISION $REPO acme
WORKDIR /opt/acme
RUN mkdir -p testing

FROM jackwolfard/acme:$TAG AS runtime

RUN apk add --no-cache bash

COPY --from=base /opt/acme/testing /opt/acme/testing
WORKDIR /opt/acme/testing
ENTRYPOINT [ "/bin/bash" ]
