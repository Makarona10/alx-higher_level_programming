#!/usr/bin/python3
"""Rectangle module"""


Base = __import__("base").Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization"""
        super().__init__(id)
        if width is not int:
            raise TypeError("width must be an integer")
        if height is not int:
            raise TypeError("height must be an integer")
        if x is not int:
            raise TypeError("x must be an integer")
        if y is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
