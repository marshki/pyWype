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

# blockdevice = blockdevice + "a"
appendBlockDevice()


