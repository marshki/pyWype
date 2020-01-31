import os
import sys

"""Placeholder.
"""

def user_is_root():
    """Check if current UID is 0.
    """

    if os.getuid() != 0:
        print("This program requires ROOT privileges. Exiting.")
        sys.exit()

user_is_root()
