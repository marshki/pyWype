#!/bin/py 

from sys import platform 

def osCheck():
	# Check if OS is UNIX-y 
	if not "darwin" or not "linux" in platform.lower():  
		print platform

osCheck()
