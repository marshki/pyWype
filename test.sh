#!/bin/bash

printf "%s\n" "FQDN: $(hostname -f)"

printf "%s\n" "DATE: $(date +%_A-%_d-%B-%Y) TIME: $(date +%R)" 

# $(+DATE: %Y-%m-%d% TIME: %H:%M:%S)"

uptime
