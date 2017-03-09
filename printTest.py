#!/bin/py 
""" Python 2.7 disk wiping utility for use on Linux OSs. """

# Import Python module 
# os module allows use of operating system-dependent functions 
import os

# Define functions 

#def osName(): 
#    """ Get OS name """
#    return os.system('uname') 

#def osCheck():
#    """ Confirm Linux stautus """

def listBlockDevices():
	""" List mounted block devices """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

def wipes(): 
    """ Prompt user for number of wipes to perform """ 
    while True: 
        try: 
            numberWipes = int(raw_input('Type the number of times you want to wipe the disk, then press Enter: '))
            return numberWipes
        except ValueError: 
            print "Sorry, that\'s not a valid number. Please try again."


listBlockDevices()
wipes()
#def selectDiskWipe()

#def numberWipes()

#def confirmWipe()

#def zeroDisk()


