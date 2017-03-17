#!/bin/py 
# Function to limit user input to 'Yes' or 'No' 

def yesOrNo(): 
    while True:
        try: 
            user_input = str(raw_input('Yes or No?: '))
            if user_input == 'Yes':
                continue 
            elif user_input == 'No': 
                break 
        except ValueError:     
            print 'That is not a valid option! Please try again'

yesOrNo()

"""
if user_input == 'Yes':
    print('You said Yes!')
else:
    print('You said No!')
"""
