#!/usr/bin/env/python3 

"""Placeholder.
"""

import re

def get_valid_user_input():
    """Prompt user to define device or partition to wipe.
    """

    while True:
        try:
            device = input(
                "Enter letter [number] of device/partition to wipe,"
                "\ne.g. to wipe '/dev/sdb1' enter 'b1': ")

            if not re.match("^[a-z][0-9]?$", device):
                raise ValueError()
            print(type(device))
            return device

        except ValueError:
            print("Sorry, that's not a valid device or partition. Try again.")

