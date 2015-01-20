#! /bin/bash
. kill.sh
killBz ./save_local.py
nohup python ./save_local.py  &
