#!/usr/bin/env python 
# Text-based menu for use in pyWype.py 

def menu(): 
    """ Menu prompt for user to select program option """

    while True: 
        print '0 - .'
        print '1 - .''
        print '2 - .' 
        print '3 - .'
        print '4.- .'

        choice = raw_input('Select an option (0, 1, 2, 3, 4): ') 

        if choice in ('0', '1', '2', '3', '4'): 
            return choice 

menu()
