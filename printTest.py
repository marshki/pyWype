#!/bin/py 

""" Python 2.7 disk wiping utility for use on Linux OSs. """

# Do we need to do a Python dependency check here? 

""" Import Python modules """
import os           # `os module` allows for use of operating system-dependent functions 
import re           # `re module` for regular expression parsing  

""" Define functions """

def osName(): 
    """ Retrieve  operating system name """
    return os.system('uname') 

#def osCheck():
#    """ Confirm Linux stautus """

def listBlockDevices():
	""" List mounted block devices """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

def defineBlockDevice(): 
    """ Prompt user to define block device """
    while True:
        try: 
            blockdevice = str(raw_input('Enter the letter of the block device you want to wipe: '))
            if not re.match("^[a-z]$", blockdevice):                                       
                raise ValueError()
            return blockdevice
        except ValueError: 
            print "Sorry, that\'s not a valid block device. Please try again."
 
def numberOfWipes(): 
    """ Prompt user for number of wipes to perform """ 
    while True: 
        try:
            wipes = int(raw_input('How many times do you want to wipe the disk?: '))
            if not wipes > 0: 
                raise ValueError()
            return wipes 
        except ValueError: 
            print "Sorry, that\'s not a valid number. Please try again."

def confirmWipe():
    """ Prompt user to confirm number of wipes """
    while True: 
        try: 
            reply = str(raw_input('Are you sure you want to proceed? (Yes/No): ')).lower().strip()
            if reply == 'yes': 
                return True              
            elif reply == 'no': 
                break 
        except ValueError: 
            print "Sorry, that\'s not a valid entry. Please try again." 
 
def zerosToDrive(): 
    """ Write zeros to drive """ 
    wipes = 1
    for int in range(1):#(numberOfWipes): 
        os.system(("dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096")) # pv -ptrb         
        wipes+=1 

def randomToDrive():
    """ Write random zeros and ones to drive """
    wipes = 1 
    for int in range(1):#(numberOfWipes):
        os.system(("dd if=/dev/random |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096")) # pv -ptrb 
        wipes+=1 

""" 
def wipeDrive(): 
     Guts of the program 
"""
osName()
listBlockDevices()
defineBlockDevice()
numberOfWipes()
confirmWipe()
zerosToDrive()
randomToDrive()
'''
if__name__ == '__main__': 
'''

