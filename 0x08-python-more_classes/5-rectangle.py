#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ This is a rectangle class """    
   
    def __init__(self, width=0, height=0):
        """initialize a rectangle object with a height 
        and width"""
        self.width = width
        self.height = height

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

    def area(self):
        """A function to calculate the area of rectangle"""
        return self.height * self.width
    
    def perimeter(self):
        """A function to return the perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2
    
    def __str__(self):
        """returns representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect = rect + (self.__width) * "#"
            if i < self.__height - 1:
                rect = rect + "\n"
        return rect
    
    def __repr__(self):
        """represent the rectangle in a formal way"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")