#!/bin/bash
python cota.py

notify-send -i face-laugh -t 3000 "$(cat ~/cota.txt)"

touch log.txt
touch date.txt
touch plog.txt
touch p.txt
ps acu >> p.txt
date >> date.txt
cat date.txt >> log.txt
cat cota.txt >> log.txt
cat date.txt >> plog.txt
cat p.txt >> plog.txt
rm p.txt
rm date.txt

exit
