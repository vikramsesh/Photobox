#!/bin/sh
sudo date -s "$(curl http://s3.amazonaws.com -v 2>&1 | grep "Date: " | awk '{ print $3 " " $5 " " $4 " " $7 " " $6 " GMT"}')"
rclone copy --progress /home/pi/Desktop/Pictures SharePoint:FSPhotobox