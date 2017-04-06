#!/usr/bin/env python  

""" Python 2.7 disk wiping utility for use on Linux operating systems. """

""" Import Python modules """

import sys              # `sys module` allows for use of variables used by the interpreter and associated functions 
import os               # `os module` allows for use of operating system-dependent functions 
import re               # `re module` allows for regular expression parsing  

""" Define functions """

def osCheck():
    """  Check if OS is 'Linux'. If not, exit. """
    if not sys.platform.startswith('linux'): 
        print 'Sorry, this program was designed for Linux. Exiting.' 
        sys.exit()

def listBlockDevices():
	""" List mounted block devices """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

def defineBlockDevice(): 
    """ Prompt user to define block device to wipe """
    
    devices = listBlockDevices() 

    while True:
        try: 
            blockdevice = str(raw_input('Enter letter of block device to be wiped, e.g. to wipe \'/dev/sdb\' enter \'b\': '))  

            if not re.match("^[a-z]$", blockdevice):                                       
                raise ValueError()
            return blockdevice
        except ValueError: 
            print 'Sorry, that\'s not a valid block device. Try again.'
 
def appendBlockDevice(): 
    """ Append user-defined block device to /dev/sd """
    
    letter = defineBlockDevice()
    
    return '/dev/sd' + letter 

def numberOfWipes(): 
    """ Prompt user for number of wipes to perform """ 
    
    while True: 
        try:
            wipes = int(raw_input('How many times do you want to wipe the disk?: '))
            ### Comments for testing to allow for zero wipes; need to remove ### 
            #if not wipes > 0: 
            #    raise ValueError()
            return wipes 
        except ValueError: 
            print 'Sorry, that\'s not a valid number. Try again.'

def warningMessage(): 
    print 'WARNING! WRITING CHANGES TO DISK: ALL DATA WILL BE LOST.' 


def confirmWipe():
    """ Prompt user to confirm disk erasure """
    
    warning = warningMessage()

    while True: 
        try: 
            reply = str(raw_input('Are you sure you want to proceed? (Yes/No): ')).lower().strip()
            if reply == 'yes': 
                return True              
            elif reply == 'no':
                sys.exit()
                 
        except ValueError: 
            print 'Sorry, that\'s not a valid entry. Try again.' 
 
def zerosToDrive(): 
    """ Write zeros to drive """ 
    
    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1 
    
    for int in range(num):
        print 'Processing pass count %s of %d ... '%(passes, num)
        os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096')) # pv -ptrb         
        passes += 1 

def randomToDrive():
    """ Write random zeros and ones to drive """
    
    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1 
    
    for int in range(num):
        print 'Processing pass count %s of %d ...'%(passes, num)
        os.system(('dd if=/dev/random |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096')) # pv -ptrb 
        passes += 1 

def wipeDrive():
    """ Prorgram to Wipe drive """ 
    
    osCheck()
    device = appendBlockDevice()  
    zero = zerosToDrive()

if __name__ == '__main__': 
    wipeDrive()
