#!/bin/py

import re

def defineBlockDevice():
    """ Prompt user to define block device """
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
    return '/dev/sd' + letter 

def numberOfWipes():                                                                                                                  
    """ Prompt user for number of wipes to perform """                                                                                
    while True:                                                                                                                       
        try:                                                                                                                          
            wipes = int(raw_input('How many times do you want to wipe the disk?: '))                                                  
            #if not wipes > 0:                                                                                                         
            #    raise ValueError()                                                                                                    
            return wipes                                                                                                              
        except ValueError:                                                                                                            
            print 'Sorry, that\'s not a valid number. Please try again.'     


def zerosToDrive():                                                                                                                   
    """ Write zeros to drive """
                                                                                                          
    num = numberOfWipes()                                                                                                             
    dev = appendBlockDevice()

    print dev 
                                                                                                                                  
    passes = 1                                                                                                                        
    for int in range(num):                                                                                                            
        print 'Processing pass count %s of %d ... '%(passes, num)                                                             
        os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=dev bs=4096')) # pv -ptrb                       
        passes+=1         

zerosToDrive()

