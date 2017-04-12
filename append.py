#!/usr/bin/env python 

import os 
import re

def listBlockDevices():
    """ List mounted block device(s) """ 
    return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

def defineBlockDevice():
    """ Prompt user to define block device """

    devices = listBlockDevices()

    while True:
        try:
            blockdevice = str(raw_input('Enter the letter of the block device you want to wipe: '))
            if not re.match("^[a-z]$", blockdevice):
                raise ValueError()
            return blockdevice

        except ValueError:
            print 'Sorry, that\'s not a valid block device. Please try again.'

def appendBlockDevice(): 
    """ Append user-defined block device to /dev/sd """ 
    letter = defineBlockDevice()
    type(letter)
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
            print 'Sorry, that\'s not a valid number. Please try again.'     


def zerosToDrive():                                                                                                                   
    """ Write zeros to drive """
    append = appendBlockDevice()
    num = numberOfWipes()                                                                                                             

    passes = 1                                                                                                                        
    for int in range(num):                                                                                                            
        print 'Processing pass count %s of %d ... '%(passes, num)                                                             
        os.system(('dd if=/dev/zero of=append bs=4096')) # pv -ptrb                       
        # os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=append bs=4096')) # pv -ptrb                       
        passes+=1         

zerosToDrive()
