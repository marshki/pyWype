#!/usr/bin/end python 

# Text-based menu for use in pyWype.py 

def menu(): 
    """ Menu prompt for user to select program option """
    while True: 
        print '0 - Single-pass zero-fill erase.'
        print '1 - Single-pass random-fill erase.'
        print '2 - US DoD 7-pass secure erase.' 
        print '3 - Gutman algorithm 35-pass secure erase.'
        print '4.- US DoE algorithm 3-pass secure erase.'

        choice = raw_input('Select an option (I, II, III, IV, V): ') 

        if choice in ('0', '1', '2', '3', '4'): 
            return choice 

menu()
