import platform
import sys

def is_linux():
    """Check if system is 'Linux'
    """
    if 'Linux' not in platform.system():
        print("This program was designed for GNU/Linux. Exiting.")
        sys.exit()

is_linux()
