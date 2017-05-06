#!/usr/bin/env python 
#!/usr/bin/env python3 

from __future__ import print_function 
from builtins import input 

""" Python 2.7 and Python 3.4 disk wiping utility for use on Linux operating systems. RUN AS ROOT. """

import sys              # For use of interpreter variables & associated functions 
import os               # For use of operating system-dependent functions 
import re               # For regular expression parsing  

""" Define functions """

def osCheck():
    """ Check if OS is 'Linux' """
    if not sys.platform.startswith('linux'):
        print('\nThis program was designed for Linux. Exiting.') 
        sys.exit()

### Need to add option to quit program at any time with keyboard combination ### 

def listDevPart():
	""" List mounted device(s) / partition(s) """ 
	return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

def defineDevPart(): 
    """ Prompt user to define device or partition to wipe """
    
    devpart = listDevPart() 

    while True:
        try: 
            devicepartition = str(input('\nEnter letter of block device to be wiped, e.g. to wipe \'/dev/sdb\' enter \'b\': '))  

            if not re.match("^[a-z]$|^[a-z]\d$", devicepartition):                                       
                raise ValueError()
            return devicepartition

        except ValueError: 
            print('\nSorry, that\'s not a valid device / partition. Try again.')
 
def appendDevPart(): 
    """ Append user-defined device/partition to /dev/sd """
    
    letter = defineDevPart()
    
    return '/dev/sd' + letter 

def numberOfWipes(): 
    """ Prompt user for number of wipes to perform """ 
    
    while True: 
        try:
            wipes = int(input('\nHow many times do you want to wipe the disk?: '))
            
            if not wipes > 0: 
                raise ValueError()
            return wipes 

        except ValueError: 
            print('\nSorry, that\'s not a valid number. Try again.')

def warningMessage(): 
    print('\nWARNING!!! WRITING CHANGES TO DISK WILL RESULT IN IRRECOVERABLE DATA LOSS.') 

def confirmWipe():
    """ Prompt user to confirm disk erasure """
    
    warning = warningMessage()

    while True: 
        try: 
            reply = str(input('\nAre you sure you want to proceed? (Yes/No): ')).lower().strip()

            if reply == 'yes': 
                return True              
            elif reply == 'no':
                sys.exit()
                 
        except ValueError: 
            print('\nSorry, that\'s not a valid entry. Try again.') 
 
def zerosToDevPart(): 
    """ Write zeros to device/partition """
 
    append = appendDevPart() 
    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1 
    
    for int in range(num):
        print('\nProcessing pass count {} of {} ... '.format(passes, num))
        os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes| dd of={} bs=4096'.format(append))) # pv -ptrb         
        passes += 1 

def randomToDevPart():
    """ Write random zeros and ones to drive """
    
    append = appendDevPart()    
    num = numberOfWipes()
    confirm = confirmWipe()

    passes = 1 
    
    for int in range(num):
        print('\nProcessing pass count {} of {} ...'.format(passes, num))
        os.system(('dd if=/dev/random |pv --progress --time --rate --bytes| dd of={} bs=4096'.format(append))) # pv -ptrb 
        passes += 1 

def menu(): 
    """ Menu prompt for use to select program option """ 
    while True: 
        print('\n1. Overwrite all sectors with zeros (Faster, less secure).')
        print('\n2. Overwrite all sectors with random data (Slower, more secure).')
        print('\n3. I want to quit.') 
        print('') 
        choice = input('Select an option (1, 2 or 3): ')

        if choice in ('1', '2', '3'): 
            return choice 

def interactiveMode(): 
    """ Display menu-driven options and return conversions. """
    while True: 
        choice = menu() 

        if choice == '3': 
            sys.exit() 
        elif choice == '1': 
            zerosToDevPart()
        elif choice == '2': 
            randomToDevPart()   

def wipeDrive():
    """ Program to Wipe drive """ 
    
    osCheck()
    interactiveMode()
    
if __name__ == '__main__':
    print('\nWelcome to pyWype. This tool will irrecoverably wipe data from your drive(s). PROCEED WITH CAUTION.') 
    wipeDrive()
