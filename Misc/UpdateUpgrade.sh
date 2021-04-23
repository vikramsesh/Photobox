#!/bin/sh
sudo apt-get update && sudo apt-get upgrade -y 
sudo apt-get autoremove 
sudo apt-get autoclean 
sudo date -s "$(curl http://s3.amazonaws.com -v 2>&1 | grep "Date: " | awk '{ print $3 " " $5 " " $4 " " $7 " " $6 " GMT"}')"
sudo reboot