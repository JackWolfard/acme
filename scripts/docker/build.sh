#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
cd $SRC_DIR/../..
ROOT_DIR=$(pwd)

DOCKER_BUILDKIT=1 docker build -t jackwolfard/acme:latest .
