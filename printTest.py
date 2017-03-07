#!/bin/py 
""" Python 2.7 disk wiping utility for use on Linux OS. """

# Import Python module 
""" os module provides a way of using operating system-dependent functions """
import os

# 

def listHardDrives():
	""" """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,SIZE,STATE,VENDOR')	
	
    # lsblk -o        
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
