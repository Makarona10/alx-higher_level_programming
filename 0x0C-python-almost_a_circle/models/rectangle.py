#!/usr/bin/python3
"""Rectangle module"""


Base = __import__("base").Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
