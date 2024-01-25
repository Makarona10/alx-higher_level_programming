#!/usr/bin/python3
def print_square(size):
    """
        prints a square with the character #

        args:
            size: The size of square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0 :
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for n in range(size):
            print("#", end="")
        print()