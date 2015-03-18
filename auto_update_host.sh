#! /bin/bash
. kill.sh
sudo killBz ./save_local.py
nohup sudo python -u ./save_local.py  &
