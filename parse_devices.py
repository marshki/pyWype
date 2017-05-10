#!/usr/bin/env python 
#!/usr/bin/env python3 

# Present to the user attached devices and partitions, where applicable 
# Allow user to select among devices 

from __future__ import print_function
from builtins import input 

import os               # For use of operating system-dependent functions  

def devPartSplash(): 
    print(66 * '-')
    print(24 * "-", "ATTACHED DEVICES", 24 * "-")
    print(66 * '-') 

def listDevPart():
        """ List mounted device(s) / partition(s) """

        splash = devPartSplash()
 
        return os.system('lsblk --nodeps --output NAME,MODEL,VENDOR,SIZE,STATE')    # lsblk -d -o NAME,MODEL,VENDOR,SIZE,STATE

listDevPart()
