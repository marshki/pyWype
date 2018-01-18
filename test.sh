#!/bin/bash

printf "%s\n" "FQDN: $(hostname -f)"

printf "%s\n" "DATE: $(date +%_A-%_d-%B-%Y) TIME: $(date +%R)" 

printf "%s\n" "UPTIME: $(uptime | awk '{print $3, $4, $5}')" 
