#!/bin/bash
file="the1000ips"
file2="theresult"


VPS=$((awk -F" " '{print $1}' ripe-vps | tail -n +2) | tr '\n' ',')

VPS=${VPS::-1}

while IFS=: read -r f1
do
        # display fields using f1, f2,..,f7

	echo $f1
#	aping --target $f1 --probes $VPS --no-report | grep http>>$file2
    aping --target $f1 --from-probes $VPS --no-report | grep http>>$file2

done <"$file"

