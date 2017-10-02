#!/bin/python 
# Check is user is logged in as root
import os 

if os.getuid() == 0: 
    print('My wish is your command')
else: 
    print('You shall not pass!')
