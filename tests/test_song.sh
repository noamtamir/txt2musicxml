#!/usr/bin/env bash

echo -en "\033[0m$1: "
crd=tests/crd_files/$1.crd
xml=tests/xml_files/$1.musicxml
if ! [ -f $crd ]; then
  { echo -e "\033[0;31mFailed. $crd is missing." >&2; exit 1; }
fi
if ! [ -f $xml ]; then
  { echo -e "\033[0;31mFailed. $xml is missing." >&2; exit 1; }
fi

result=$(poetry run python txt2musicxml/main.py < tests/crd_files/$1.crd | tr -d '[:space:]')
expected=$(cat tests/xml_files/$1.musicxml | tr -d '[:space:]')

set -e
if [[ "$result" != "$expected" ]]; then
    { echo -e "\033[0;31mFailed" >&2; exit 1; }
else
    echo -e "\033[0;32mSuccess"
fi
