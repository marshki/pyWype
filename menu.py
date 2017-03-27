#!/usr/bin/end python 

# Text-based menu for use in pyWype.py 

def menu(): 
    """ Menu prompt for user to select program option """
    while True: 
        print 'I'
        print 'II'
        print 'III' 
        print 'IV'
        print 'V'

        choice = raw_input('Select an option (I, II, III, IV, V): ') 

        if choice in ('I', 'II', 'III', 'IV', 'V'): 
            return choice 

menu()
