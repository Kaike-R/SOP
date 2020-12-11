#!/bin/bash
python cota.py

notify-send -i face-laugh -t 3000 "$(cat ~/cota.txt)"

exit
