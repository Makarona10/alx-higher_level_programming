#!/usr/bin/python3
"""look up module"""


def lookup(obj):
    """Lookup function
    
        Args:
            obj: The object we will return its attributes

        Return: List of an object attributes
    """
    
    return dir(obj)