#!/bin/bash

printf "%s\n" "FQDN: $(hostname -f)"

printf "%s\n" "DATE: $(date +%_A-%_d-%B-%Y) TIME: $(date +%R)" 

printf "%s\n" "UPTIME: $(uptime | tr -d ',' |awk '{print $3, $4, $5}')"

printf "%s\n" "MEMORY: $()" 

printf "%s\n" "DISK USAGE: $()"

printf "%s\n" "LOAD AVERAGES: $()" 

printf "%s\n" "RUNNING PROCESSES: $()" 

printf "%s\n" "IP ADDRESS: $()" 
 
