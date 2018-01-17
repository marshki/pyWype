#!/bin/bash

printf "%s\n" "FQDN: $(hostname -f)"

printf "%s\n" "DATE: $(date +%A-%d-%B-%Y-%R)" 

# $(+DATE: %Y-%m-%d% TIME: %H:%M:%S)"

uptime
