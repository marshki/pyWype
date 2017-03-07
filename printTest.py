#!/bin/py 
""" Python 2.7 disk wiping utility for use on Linux OS. """

# Import Python module 
# os module allows use of operating system-dependent functions 
import os

# Define functions 

def osName(): 
    """ Get OS name """
    return os.system('uname') 

def listBlockDevices():
	""" List mounted block devices """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

osName()
listBlockDevices()

#def selectDiskWipe()

#def numberWipes()

#def confirmWipe()

#def zeroDisk()


