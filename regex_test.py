#!/usr/bin/env python 

import re 

def defineBlockDevice():
    """ Prompt user to define block device to wipe """

    while True:
        try:
            blockdevice = str(raw_input('Enter letter of block device to be wiped, e.g. to wipe \'/dev/sdb\' enter \'b\': '))

            # if not re.match("^[a-z]$", blockdevice): 
            if not re.match("^[a-z]$|^[a-z]\d$", blockdevice):
                raise ValueError()
            return blockdevice

        except ValueError:
            print 'Sorry, that\'s not a valid block device. Try again.'

defineBlockDevice()
