#!/bin/py 
import re 

def stringCheck():                                                                                                                     
    """ ABC check """                                                                                                                 
    while True:                                                                                                                     
        try: 
            stringy = raw_input("block device: ")                                                                                     
            return stringy                                                                                                            
        except ValueError:
            print "Sorry, that\'s not a valid character."  


stringCheck()
stringCheck()
stringCheck()
stringCheck()
