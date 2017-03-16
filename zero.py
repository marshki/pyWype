#!/bin/py 
import os 

count = 2 

def zeroToDrive():
    ''' write zeros to drive '''
    wipes = 1 
    for int in range(count): 
        os.system(("dd if=/dev/zero of=/dev/null"))
        wipes+=1 
zeroToDrive()
        
