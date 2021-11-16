#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
TEST_DIR="${SRC_DIR}/../errors"
TMP="/tmp/docker-error"

cd "${TEST_DIR}"

echo "ACME Docker: errors test start"

for file in *.a; do
  if [[ -f "${file}" ]]; then
    acme "${file}" 2> "${TMP}"
    ACME_CODE=$?
    cat "${TMP}" | grep "Error"
    GREP_CODE=$?
    if [[ (( ${ACME_CODE} == 0 || ${GREP_CODE} != 0 )) ]]; then
      echo "ACME Docker: errors test failure"
      exit 1
    fi
  fi
done

echo "ACME Docker: errors test success"

exit 0
