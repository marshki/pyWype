#!/usr/bin/env python 

#Imports OS functions
import os

#The function for writing a disk with zeros.
def zero():
    print ""
    os.system("/sbin/fdisk -l")
    print ""
    print "Please choose a device to wipe. Remember if you want to"
    print "wipe the whole drive and not just a partition, you can"
    print "remove the number appended.  Example /dev/sdc1 becomes /dev/sdc ."
    print ""
    device=raw_input("Enter device: ")
    print ""
    count=input("How many times would you like to wipe the device? ")
    print ""
    print "Writing changes to disk.  All data on %s will be lost."%(device)
    print ""
    raw_input("Press Enter to continue, or Ctrl+C to exit: ")
    print ""
    lap=1
    for i in range(count):
        print "Processing wipe count %s of %s..."%(lap, count)
        os.system(("dd if=/dev/zero of=%s")%(device))
        lap=lap+1

#The function for writing random data to the disk.
def random():
    print ""
    os.system("/sbin/fdisk -l")
    print ""
    print "Please choose a device to wipe. Remember if you want to"
    print "wipe the whole drive and not just a partition, you can"
    print "remove the number appended.  Example /dev/sdc1 becomes /dev/sdc ."
    print ""
    device=raw_input("Enter device: ")
    print ""
    count=input("How many times would you like to wipe the device? ")
    print ""
    print "Writing changes to disk.  All data on %s will be lost."%(device)
    print ""
    raw_input("Press Enter to continue, or Ctrl+C to exit: ")
    print ""
    lap=1
    for i in range(count):
        print "Processing wipe count %s of %s..."%(lap, count)
        os.system(("dd if=/dev/urandom of=%s")%(device))
        lap=lap+1

#Main function
def main():
    if os.name!="posix":
        print "This program is designed to run only on Unix like"
        print "operating systems."
        print ""
        raw_input("Press Enter to exit...")
        exit
    print ""
    print "This program will erase any disk or partition you specify."
    print "At any time you can press Ctrl+C to cancel the program."
    print "If you do so before a wipe operation has begun, no changes"
    print "will have been made to the drive."
    print ""
    raw_input("Press Enter to continue...")
    print ""
    print "What type of wipe would you like to perform? "
    print ""
    print "1) Overwrite all sectors with zeros (Faster, less secure)"
    print "2) Overwrite all sectors with random data (Slower, more secure)"
    print ""
    style=raw_input("Enter a number: ")
    if style=="1":
        zero()
    elif style=="2":
        random()
    else:
        print "Invalid input, exiting program to avoid unwanted"
        print "damage to a hard drive."
        print ""
        raw_input("Press Enter to exit...")
        exit

#Checks the Operating System
def firstrun():
    if os.name!="posix":
        print "This program is designed to run only on Unix like"
        print "operating systems."
        print ""
        raw_input("Press Enter to exit...")
        exit
    else:
        main()
firstrun()
