#!/usr/bin/python3
"""Rectangle module"""


Base = __import__("base").Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
            """Calculates the area of a rectangle"""
            return self.__height * self.__width
        
    def display(self):
        """prints in stdout the Rectangle instance"""
        if self.__width == 0 or self.__height == 0:
                print()
        else:
            for x in range (self.__y):
                print()
            for i in range (self.__height):
                for y in range (self.__x):
                    print(" ", end="")
                for m in range (self.__width):
                    print("#", end="")
                print()
        
    def __str__(self):
        """Returns informal representation of a rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        if args[0]:
            self.id = args[0]
        if args[1]:
            self.__width = args[1]
        if args[2]:
            self.__height = args[2]
        if args[3]:
            self.__X = args[3]
        if args[4]:
            self.__y = args[4]
        