#!/usr/bin/python3
"""Is same class module"""


def is_same_class(obj, a_class):
    """Checks if the instance is form a particular class"""

    if type(obj) != a_class:
        return False
    else:
        return True