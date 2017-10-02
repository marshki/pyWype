#!/bin/py 
# check if POSIX

import os 

def osCheck():
    if 'posix' not in os.name:		
        print("Non-POSIX system detected")

osCheck()
