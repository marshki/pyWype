#!/usr/bin/env python 

import sys 


def osCheck(): 
    """ Check if system is running 'Linux' """
    return sys.platform.startswith('linux')
    
def isLinux(): 
    os = osCheck()
    print os 
 

osCheck()
isLinux()
