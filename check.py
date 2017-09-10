#!/bin/py

import os
import sys

def osCheck():
    """ Check if OS is 'UNIX-like' """
    if not sys.platform.startswith('linux') or sys.platform.startswith('darwin'):  
    # if not sys.platform.startswith('darwin'):
        print("This program was designed for UNIX-like systems. Exiting.") 
        sys.exit()

osCheck()
