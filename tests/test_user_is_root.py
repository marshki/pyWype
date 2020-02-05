#!/usr/bin/env python3

"""Placeholder.
"""

import os
import sys


def user_is_root():
    """Check if current UID is 0.
    """

    if os.getuid() != 0:
        print("This program requires ROOT privileges. Exiting.")
        sys.exit()

user_is_root()
