#!/usr/bin/env


def menu():
    """Menu prompt for user to select program option"""
    while True:
        print '1. Overwrite all sectors with zeros (Faster, less secure).'
        print '2. Overwrite all sectors with random data (Slower, more secure).'
        print '3. I want to quit.'
        print()
        choice = input('Select an option (1, 2 or 3):  ')
        if choice in ('1','2','3'):
            return choice
