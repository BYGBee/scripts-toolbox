#!/bin/bash

#This is a small bash script created to check if web interface of devices are available within a machine.
#Call this script from bashrc and check the line when opening a prompt. If a 0 appears, there is a problem with one device.

today="$(date) - "

URL=("https://www.google.com/" "https://www.google.com/")

for str in ${URL[@]}; do
    if wget --spider "${URL}" 2>/dev/null;
    then
        #echo "This page still exists."
        check=1
    else
        #echo "This page does not exists anymore."
        check=0
    fi
    today="$today$check"
done

echo "$today"
