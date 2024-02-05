#!/usr/bin/python3
"""Inheritence module"""

class MyList(list):
    """MyList class"""

    def __init__(self):
        """For MyList initialization"""
        super.__init()

    def print_sorted(self):
        """prints the list (sorted)"""
        print(sorted(self))
