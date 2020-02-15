#!/usr/bin/env/python3

"""Placeholder.
"""

import platform
import sys
import unittest
from unittest.mock import patch

def is_linux():
    """Check if system is 'Linux'
    """
    if 'Linux' not in platform.system():
        print("This program was designed for GNU/Linux. Exiting.")
        sys.exit()
"""
class CheckOS(unittest.TestCase):
    #Unit test.

    @patch('platform.system', return_value='Darwin')
    def test_is_linux(self, system):
        """Placeholder.
        """
        self.assertEqual(is_linux(), 'Darwin')
"""

if __name__ == '__main__':
    unittest.main()
