#!/usr/bin/env python 

# Import Python module 
import os 

def osCheck():
	""""Check if OS is UNIX-like."""
	if os.name !='posix': 
		print "pyWipe will ONLY run on UNIX-like systems."
	else: 
		print "Let there be wipe!"

osCheck()
