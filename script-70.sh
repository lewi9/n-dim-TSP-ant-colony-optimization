#!/bin/bash
i=0
while IFS=" " read -a fields; do
    printf "%s\t" "${fields[@]}";
    i=$(($i+1))
    if [ "$i" == "8" ] ; then
	    printf "\n"
	    i=0
    fi
done < 4.txt
