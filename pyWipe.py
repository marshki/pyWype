#!/usr/bin/env python  

""" Python 2.7 disk wiping utility for use on Linux operating systems. """

""" Import Python modules """

import sys              # For use of interpreter variables & associated functions 
import os               # For use of operating system-dependent functions 
import re               # For regular expression parsing  

""" Define functions """

def osCheck():
    """ Check if OS is 'Linux' """
    if not sys.platform.startswith('linux'):
        print 'Sorry, this program was designed for Linux. Exiting.' 
        sys.exit()

def listBlockDevices():
	""" List mounted block device(s) """ 
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
            
            if not wipes > 0: 
                raise ValueError()
            return wipes 

        except ValueError: 
            print 'Sorry, that\'s not a valid number. Try again.'

def warningMessage(): 
    print 'WARNING!!! WRITING CHANGES TO DISK WILL RESULT IN IRRECOVERABLE DATA LOSS.' 

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
 
    append = appendBlockDevice() 
    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1 
    
    for int in range(num):
        print 'Processing pass count %s of %d ... '%(passes, num)
        os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096')) # pv -ptrb         
        passes += 1 

def randomToDrive():
    """ Write random zeros and ones to drive """
    
    append = appendBlockDevice()    
    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1 
    
    for int in range(num):
        print 'Processing pass count %s of %d ...'%(passes, num)
        os.system(('dd if=/dev/random |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096')) # pv -ptrb 
        passes += 1 

def menu(): 
    """ Menu prompt for use to select program option """ 
    while True: 
        print '1. Overwrite all sectors with zeros (Faster, less secure).'
        print '2. Overwrite all sectors with random data (Slower, more secure).'
        print '3. I want to quit.' 
        print '' 
        choice = raw_input('Select an option (1, 2 or 3): ')

        if choice in ('1', '2', '3'): 
            return choice 

def interactiveMode(): 
    """ Display menu-driven options and return conversions. """
    while True: 
        choice = menu() 

        if choice == '3': 
            sys.exit() 
        elif choice == '1': 
            zerosToDrive()
        elif choice == '2': 
            randomToDrive()   

def wipeDrive():
    """ Prorgram to Wipe drive """ 
    
    osCheck()
    interactiveMode()
    
if __name__ == '__main__': 
    wipeDrive()
