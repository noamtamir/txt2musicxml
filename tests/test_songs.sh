#!/usr/bin/env bash
echo "Testing songs"
echo "============="
readarray -t songs < tests/test_song_names.txt
for song in "${songs[@]}";
do
    (./tests/test_song.sh $song);
done