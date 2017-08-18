#!/usr/bin/env python 
# Simplify randomToDevice, zerosToDevice functions
# This seems to work 2017.08.18

def numWipes(): 
	""" Number of wipes """ 
	wipes = int(input("Number of wipes? : "))
	return wipes 

def passCount(): 
    """ Keep track on number of passes performed """
  
num  = numWipes()

for int in range(num): 
    print("Processing pass count {} of {} ...".format(int + 1, num))

passCount()
