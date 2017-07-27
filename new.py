#!/usr/bin/env python
#!/usr/bin/env python3

from __future__ import print_function
from builtins import input

""" Python 2.7 &  3.4 disk wiping utility for use on Linux operating systems. RUN AS ROOT. """

import sys              # For interpreter variables & associated functions
import os               # For operating system-dependent functions
import re               # For regular expression parsing

def devPartHeader():
    """ Header for attached device(s) / partition(s) """
    print(24 * "-", "ATTACHED DEVICES", 24 * "-")

def listDevPart():
    """ List mounted device(s) / partition(s) """

    header = devPartHeader()

    return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')      #lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE


