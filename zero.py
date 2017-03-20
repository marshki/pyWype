#!/bin/py 
import os 

count = 1 

def zeroToDrive():
    ''' write zeros to drive '''
    wipes = 1 
    for int in range(count): 
        os.system(("dd if=/dev/zero |pv --progress --timer --rate --bytes| dd of=/dev/null bs=4096"))
        # os.system(os.system(("dd if=/dev/zero| pv -ptrb | dd of=/dev/null bs=4096"))
        wipes+=1 
zeroToDrive()
