#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
TEST_DIR="${SRC_DIR}/../cpus"

cd "${TEST_DIR}"

echo "ACME Docker: cpus test start"

bash "./check-all-cpus.sh"

if [[ $? -eq 0 ]]; then
  echo "ACME Docker: cpus test success"
  exit 0
fi

echo "ACME Docker: cpus test failure"
exit 1
