#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
cd $SRC_DIR/../../..
ROOT_DIR=$(pwd)
TEST_DIR="${ROOT_DIR}/tests/docker"
TAG="latest"
cd $TEST_DIR

echo "ACME Docker: starting testing container"

docker run --rm -it \
  -v "${TEST_DIR}":/opt/acme/testing/docker \
  --entrypoint "/opt/acme/testing/docker/all.sh" \
  "jackwolfard/acme-tests:${TAG}" 

CODE=$?

if [[ ${CODE} -ne 0 ]]; then
  echo "ACME Docker: testing container failure"
  exit ${CODE}
fi

echo "ACME Docker: testing container success"
exit ${CODE}

