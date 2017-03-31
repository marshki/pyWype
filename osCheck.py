#!/usr/bin/env python 

import os 
from sys import platform 

def osName(): 
    """ Retrieve operating system name """
    return os.system('uname') # o 

def osCheck(): 
    # from sys import platform
    if platform == "linux" or platform == "linux2":
        print 'linux'
    elif platform == "darwin":
        print 'OS X'
    elif platform == "win32":
        print 'Windows'
       
osCheck()
