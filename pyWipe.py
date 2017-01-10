from builtins import input 

#!/usr/bin/env python 

"""Python program for filling hard drives with either zeros (0s),  or zeros (0s) and ones (1s). Designed and tested to work with POSIX-compliant Linux systems ONLY."""

# Import Python module 

import os					# os function allows Python to interact with operating system-dependent functions   

# Define functions 

def osCheck():
	"""Check OS for POSIX"""
	if os.name =='posix': 
		print('OK. Let\'s proceed!')
	else: 
		print('Sorry, invalid system. Can not proceed.')

osCheck()
'''   
def zeroOutDisk():
	"""Fill selected device (/dev/) with zeros.""" 

def randomWriteDisk(): 
	"""Fill selected device (/dev/) with zeros and ones." 

def menu(): 
	"""Menu prompt."""

def main(): 
	"""Main function."""
'''
