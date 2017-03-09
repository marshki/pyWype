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
            numberWipes = int(raw_input('How many times do you want to wipe the disk?: '))
            return numberWipes
        except ValueError: 
            print "Sorry, that\'s not a valid number. Please try again."

def confirm():
    """ Prompt user to confirm wipe process """
    while True: 
        try: 
            reply = str(raw_input('Are you sure you want to proceed? (Yes/No): ')).lower().strip()
            if reply == 'yes': 
                return True 
            if reply == 'no': 
                return False 
        except ValueError: 
            print "Sorry, that\'s not a valid entry. Please try again." 
 

listBlockDevices()

wipes()

confirm()
#def selectDiskWipe()

#def numberWipes()

#def confirmWipe()

#def zeroDisk()


