#!/bin/py 

import re 

def stringCheck():                                                                                                                     
    """ ABC check """                                                                                                                 
    while True:                                                                                                                     
        try:
            stringy =  str(raw_input("Enter block device: "))
            # if len(stringy) != 1:  
            if not re.match("^[a-z]$", stringy): # or len(stringy) != 1:                 
                raise ValueError()
            return stringy 
        except ValueError:
            print "Sorry, that\'s not a valid entry. Please try again."  

stringCheck()

