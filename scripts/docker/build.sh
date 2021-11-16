#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
cd $SRC_DIR/../..
ROOT_DIR=$(pwd)

: "${TAG:=latest}"
: "${REPO:=https://svn.code.sf.net/p/acme-crossass/code-0/trunk}"
: "${REVISION:=323}"

DOCKER_BUILDKIT=1 docker build -t "jackwolfard/acme:${TAG}" \
  --build-arg REPO="${REPO}" --build-arg REVISION="${REVISION}" .
