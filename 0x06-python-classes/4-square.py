#!/usr/bin/python3
""" Square doc """


class Square:
    """ This is a square class """

    def __init__(self, size=0):
        """
        Initializes class attributes

        args:
            size: size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        Calculates the area of square
        
        Returns:
            the calculated area
        """
        return self.__size**2
    @property
    def size(self):
        """Retrieves square size"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """
        Set the size of square
        
        agrs:
            value: The new value of size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
