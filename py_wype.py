#!/usr/bin/env python3

"""Disk-wiping utility.
"""

from __future__ import print_function

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

from builtins import input
import sys
import os
import re

def posix_os_check():
    """Check if OS is 'POSIX'.
    """

    if 'posix' not in os.name:
        print("This program was designed for Linux. Exiting.")
        sys.exit()

def root_user_check():
    """Check is current user has UID 0.
    """

    if not os.getuid() == 0:
        print("This program requires ROOT privileges. Exiting.")
        sys.exit()

def list_mounted_devices():
    """List mounted device(s) / partition(s).
    lsblk -d -o NAME.MODEL,VENDOR...
    """

    print(22 * "-", "DEVICES & PARTITIONS", 22 * "-")

    return os.system('lsblk /dev/sd* --nodeps --output NAME,MODEL,VENDOR,SIZE,TYPE,STATE')

def define_device_to_wipe():
    """Prompt user to define device or partition to wipe.
    """

    while True:
        try:
            device = str(input(
                "Enter letter [number] of device/partition to wipe,"
                "\ne.g. to wipe '/dev/sdb1' enter 'b1': "))

            if not re.match("^[a-z][0-9]?$", device):
                raise ValueError()
            return device

        except ValueError:
            print("Sorry, that's not a valid device or partition. Try again.")

def append_device_to_wipe():
    """Append user-defined device/partition to /dev/sd.
    """

    letter = define_device_to_wipe()

    return '/dev/sd' + letter

def number_of_wipes():
    """Prompt user for number of wipes to perform.
    """

    while True:
        try:
            wipes = int(input("How many times do you want to wipe the device or partition?: "))

            if wipes <= 0:
                raise ValueError()
            return wipes

        except ValueError:
            print("Sorry, that's not a valid number. Try again: ")

def confirm_wipe():
    """Prompt user to confirm disk erasure.
    """

    print("WARNING!!! WRITING CHANGES TO DISK WILL RESULT IN IRRECOVERABLE DATA LOSS.")

    while True:
        try:
            reply = str(input("Are you sure you want to proceed? (Yes/No): ")).lower().strip()

            if reply == 'yes':
                return True
            if reply == 'no':
                print("Exiting pyWype.")
                sys.exit()

        except ValueError:
            print("Sorry, that's not a valid entry. Try again: ")

def write_zeros_to_device():
    """Write zeros to device/partition.
    pv -ptrb
    """

    append = append_device_to_wipe()
    num = number_of_wipes()
    confirm_wipe()

    for i in range(num):
        print("Processing pass count {} of {} ... ".format(i + 1, num))
        os.system(('dd if=/dev/zero |pv --progress --time --rate --bytes|'
                   'dd of={} bs=1024'.format(append)))

def write_random_to_device():
    """Write random zeros and ones to device/partition.
    """

    append = append_device_to_wipe()
    num = number_of_wipes()
    confirm_wipe()

    for i in range(num):
        print("Processing pass count {} of {} ... ".format(i + 1, num))
        os.system(('dd if=/dev/urandom |pv --progress --time --rate --bytes|'
                   'dd of={} bs=1024'.format(append)))

def menu():
    """Menu prompt for use to select program option.
    """

    list_mounted_devices()

    while True:
        try:
            print(30 * "-", "MENU", 30 * "-")
            print("1. Overwrite device or partition with 0's \n(faster, less secure).")
            print("2. Overwrite device or partition with random 0\'s & 1\'s"
                  "\n(slower, more secure).")
            print("3. Quit.")

            choice = input("Select an option (1, 2 or 3): ")

            if choice not in ('1', '2', '3'):
                raise ValueError()
            return choice

        except ValueError:
            print("Sorry, that's not a valid number. Try again: ")

def interactive_mode():
    """Display menu-driven options and run function based on selection.
    """

    while True:
        choice = menu()

        if choice == '3':
            sys.exit()
        elif choice == '1':
            write_zeros_to_device()
        elif choice == '2':
            write_random_to_device()

def wipe_device():
    """Program to wipe drive.
    """

    posix_os_check()
    root_user_check()
    interactive_mode()

if __name__ == '__main__':
    print(28 * '-', " pyWype ", 28 * '-')
    print("PYTHON DISK & PARTITION WIPING UTILITY FOR LINUX."
          "\nTHIS WILL IRRECOVERABLY WIPE DATA FROM DRIVE.\nPROCEED WITH CAUTION.")

    wipe_device()
