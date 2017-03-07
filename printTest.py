#!/bin/py 

#Import OS functions 
import os

def listHardDrives(): 
	print(
		"""
		os.system("/sbin/fdisk -l")
		"""
	) 





print(
"""

Please choose a device to kill. 
Remember if you want wipe the whole drive and not just a partition,
you can remvoe the number appended. 

"""
)
