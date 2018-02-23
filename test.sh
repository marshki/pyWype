#!/bin/bash

printf "%s\n" "FQDN: $(hostname -f)"

printf "%s\n" "DATE: $(date +%_A-%_d-%B-%Y) TIME: $(date +%R)"

printf "%s\n" "UPTIME: $(uptime | tr -d ',' |awk '{print $3, $4, $5}')"

if [ "$OSTYPE" == "linux-gnueabihf" ]; then
  	printf "%s\n" "MEMORY: $(free -gh)"
else [ "$OSTYPE" == "darwin"* ];
	printf "%s\n" "MEMORY: $(top -l 1 -s 0 | grep PhysMem)"
fi

printf "%s\n" "DISK USAGE: $()"

# $DISK_USED=df -h | grep 'dev/root' | awk '{print $3}'  | xargs 
# $DISK_FREE=df -h | grep 'dev/root' | awk '{print $3}'  | xargs 


#rintf "%s\n" "LOAD AVERAGES: $()"

#printf "%s\n" "RUNNING PROCESSES: $()"

#printf "%s\n" "IP ADDRESS: $()"
