#!/bin/bash
# Message of the Day for Raspberry Pi 

# System Uptime 
 
let upSeconds="$(/usr/bin/cut -d. -f1 /proc/uptime)"
let secs=$((${upSeconds}%60))
let mins=$((${upSeconds}/60%60))
let hours=$((${upSeconds}/3600%24))
let days=$((${upSeconds}/86400))
UPTIME=`printf "%d days, %02dh%02dm%02ds" "$days" "$hours" "$mins" "$secs"`

# Free/Total System RAM 

MEMFREE=`cat /proc/meminfo | grep MemFree | awk {'print $2'}`
MEMTOTAL=`cat /proc/meminfo | grep MemTotal | awk {'print $2'}`

# Used/Available Disk Space 

SDUSED=`df -h | grep 'dev/root' | awk '{print $3}'  | xargs`
SDAVAIL=`df -h | grep 'dev/root' | awk '{print $4}'  | xargs`

# CPU Load Averages

read one five fifteen rest < /proc/loadavg

# Define GUI Palette
# Need to change the color scheme using tput code: 
# 0 – Black.
# 1 – Red.
# 2 – Green.
# 3 – Yellow.
# 4 – Blue.
# 5 – Magenta.
# 6 – Cyan.
# 7 – White. 

DARKGREY="$(tput sgr0 ; tput bold ; tput setaf 0)"
RED="$(tput sgr0 ; tput setaf 1)"
GREEN="$(tput sgr0 ; tput setaf 2)"
BLUE="$(tput sgr0 ; tput setaf 4)"
BLACK="$(tput sgr0 ; tput setaf 7)"
NC="$(tput sgr0)" # No Color

# ASCII ART 

echo "${DARKGREY}
   .~~.   .~~.    `hostname -f`
  '. \ ' ' / .'   `date +"%A, %e %B %Y, %r"`${DARKGREY}
   .~ .~~~..~.
  : .~.'~'.~. :   ${DARKGREY}Uptime.............: ${BLUE}${UPTIME}${RED}
 ~ (   ) (   ) ~  ${DARKGREY}Memory.............: ${BLUE}${MEMFREE}kB (Free) / ${MEMTOTAL}kB (Total)${RED}
( : '~'.~.'~' : ) ${DARKGREY}Disk usage.........: ${BLUE}${SDUSED} (Used) / ${SDAVAIL} (Free)${RED}
 ~ .~ (   ) ~. ~  ${DARKGREY}Load Averages......: ${BLUE}${one}, ${five}, ${fifteen} (1, 5, 15 min)${RED}
  (  : '~' :  )   ${DARKGREY}Running Processes..: ${BLUE}`ps ax | wc -l | tr -d " "`${RED}
   '~ .~~~. ~'    ${DARKGREY}IP Addresses.......: ${BLUE}`hostname -I`${RED}
       '~'
${NC}"
