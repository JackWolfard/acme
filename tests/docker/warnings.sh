#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
TEST_DIR="${SRC_DIR}/../warnings"
TMP="/tmp/docker-warnings"

cd "${TEST_DIR}"

echo "ACME Docker: warnings test start"

for file in *.a; do
  if [[ -f "${file}" ]]; then
    acme "${file}" 2> "${TMP}"
    ACME_CODE=$?
    cat "${TMP}" | grep "Warning"
    GREP_CODE=$?
    if [[ (( ${ACME_CODE} != 0 || ${GREP_CODE} != 0 )) ]]; then
      echo "ACME Docker: warnings test failure"
      exit 1
    fi
  fi
done

echo "ACME Docker: warnings test success"

exit 0
