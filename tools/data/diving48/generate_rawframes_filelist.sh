#!/usr/bin/env bash

cd ../../../
PYTHONPATH=. python tools/data/build_file_list.py diving48 data/diving48/rawframes/ --num-split 1 --level 1 --subset train --format rawframes --shuffle --seed 9
PYTHONPATH=. python tools/data/build_file_list.py diving48 data/diving48/rawframes/ --num-split 1 --level 1 --subset val --format rawframes --shuffle --seed 9
echo "Filelist for rawframes generated."

cd tools/data/diving48/
