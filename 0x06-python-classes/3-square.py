#!/usr/bin/python3
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
        """ Returns the area of square """
        return (self.__size)*(self.__size)
