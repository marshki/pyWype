#!/bin/py 

#from sys import platform 
import os 

def osCheck():
	# Check if OS is UNIX-y 
	if 'posix' not in os.name:		
            print("Non-POSIX system detected")

osCheck()
