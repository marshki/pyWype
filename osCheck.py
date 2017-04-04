#!/usr/bin/env python 

import sys 


def osCheck(): 
    """ Check if system is running 'Linux' """
    if not sys.platform.startswith('linux'): 
        print 'Sorry, we can\'t continue. Ciao' 
        sys.exit()

osCheck()


