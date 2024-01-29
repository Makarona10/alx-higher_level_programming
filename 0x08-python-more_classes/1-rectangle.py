#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ This is a rectangle class """    
   
    def __init__(self, width=0, height=0):
        """initialize a rectangle object with a height 
        and width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """a function to retrieve the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A function to set width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A function to retrieve the rectangle height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """A function to set the rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value