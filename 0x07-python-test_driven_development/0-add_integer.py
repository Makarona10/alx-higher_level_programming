#!/usr/bin/python3
"""add integer module"""


def add_integer(a, b=98):
    """
    A function adds two integers

    args: 
        a: first integer to add 
        b: second integer to add

    Return: The addition of 2 integers 
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)