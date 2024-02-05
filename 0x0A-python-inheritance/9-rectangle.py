#!/usr/bin/python3
"""Rectangle Module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle Module """


    def __init__(self, width, height):
        """Rectangle initialization"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)