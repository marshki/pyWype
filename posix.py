#!/bin/py 

from sys import platform 

def osCheck():
	# Check if OS is UNIX-y 
	if "darwin" or "linux" in platform.lower():  
		print platform

osCheck()
