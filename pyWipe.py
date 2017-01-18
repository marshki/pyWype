from builtins import input 

#!/usr/bin/env Python3
# Python 2 & 3 

''' Python program to fill storage device(s)  with either zeroes(0s), or a random pattern of zeroes(0s) and ones (1s). '''

# Import os functions
import os

def userFloat(): 
    '''Prompt user for input, accepting only valid input.'''
    while True: 
        try: 
            return float(input('How many times would you like to wipe this device?: '))
        except ValueError: 
            print('Bad value, try again.')

def osCheck():
	'''Check if OS is UNIX-like.'''
	if os.name =='posix': 
        print('Proceed')
    else: 
        print('Halt')

def zeroDisk(): 
    '''Fill disk with zeros (0s).'''
    return os.system('dd if=/dev/zero')

def randomDisk(): 
    '''Fill disk with random sequence of zeros (0s) and (1s).'''
    return os.system('dd if=/dev/random')
