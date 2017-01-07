#!/usr/bin/env python3 

# Import Python module 
import os 

def osCheck():
	""""Check if OS is UNIX-like."""
	if os.name =='posix': 
		print('Let there be wipe!') 
	else: 
		print('NOT POSIX-compliant, can not proceed.')

osCheck()
