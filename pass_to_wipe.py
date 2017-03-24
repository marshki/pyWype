#!/bin/py 
# testing 

import os 

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

def zerosToDrive():
    """ Write zeros to drive """
    num = numberOfWipes()
    
    wipes = 1
    for int in range(num):
        print "Processing wipe count %s of %d ..."%(wipes, num) 
        os.system(("dd if=/dev/zero |pv --progress --time --rate --bytes| dd of=/dev/null bs=4096")) # pv -ptrb         
        wipes+=1

zerosToDrive()
