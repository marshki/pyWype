#!/usr/bin/env python
#!/usr/bin/env python3 

"""
Unit tests
"""

import unittest 
from pyWipe import 

def defineDevPart():
    """ Prompt user to define device or partition to wipe """

    # devpart = listDevPart()

    while True:
        try:
            devicepartition = str(input('Enter letter of block device to be wiped, e.g. to wipe \'/dev/sdb\' enter \'b\': '))

            if not re.match("^[a-z]$|^[a-z]\d$", devicepartition):
                raise ValueError()
            return devicepartition

        except ValueError:
            print('Sorry, that\'s not a valid device / partition. Try again.')

