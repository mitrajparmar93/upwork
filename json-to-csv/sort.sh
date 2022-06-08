#!/usr/bin/env bash

DATAFILE="out.json"

i=0

while read -r line; do

    ((i++))
    mkdir -p data && touch "data/file-${i}.json"
    echo ${line} >"data/file-${i}.json"

done <"${DATAFILE}"