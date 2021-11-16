#!/usr/bin/env bash

SRC_DIR=$(echo ${0%/*} | xargs realpath)
cd ${SRC_DIR}

echo "ACME Docker: all test start"

bash ./cpus.sh
CPUS=$?
bash ./warnings.sh
WARNINGS=$?
bash ./errors.sh
ERRORS=$?

if [[ (( ${CPUS} != 0 || ${WARNINGS} != 0 || ${ERRORS} != 0 )) ]]; then
  echo "ACME Docker: all test failure"
  exit 1
fi

echo "ACME Docker: all test success"
exit 0
