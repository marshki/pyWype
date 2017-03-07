#!/bin/py 

#Import OS functions 
import os

def listHardDrives(): 
    return os.system("lsblk --output NAME,FSTYPE,LABEL,UUID,MODE")
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
