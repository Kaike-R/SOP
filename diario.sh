#!/bin/bash
python cota.py

notify-send -i face-laugh -t 3000 "$(cat ~/cota.txt)"

touch log.txt
cp cota.txt log.txt

exit
