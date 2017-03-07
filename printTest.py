#!/bin/py 
""" Python 2.7 disk wiping utility for use on Linux OS. """

# Import Python module 
# os module allows use of operating system-dependent functions 
import os

# 

def listHardDrives():
	""" List block devices """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,SIZE,STATE,VENDOR')    # lsblk -d -o NAME,MODEL,SIZE,STATE,VENDOR

listHardDrives()

#def selectDiskWipe()

#def numberWipes()

#def confirmWipe()

#def zeroDisk()



#print(
#"""

#Please choose a device to kill. 
#Remember if you want wipe the whole drive and not just a partition,
#you can remvoe the number appended. 

#"""
#)
