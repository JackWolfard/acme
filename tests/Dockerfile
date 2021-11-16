FROM jackwolfard/acme:latest AS base

RUN apk add --no-cache subversion
WORKDIR /opt
RUN svn checkout https://svn.code.sf.net/p/acme-crossass/code-0/trunk acme

FROM jackwolfard/acme:latest AS runtime

COPY --from=base /opt/acme/testing /opt/acme/testing
WORKDIR /opt/acme/testing
ENTRYPOINT [ "/bin/sh" ]
