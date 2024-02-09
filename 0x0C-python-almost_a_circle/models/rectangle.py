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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculates the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance"""
        if self.width == 0 or self.height == 0:
            print()
        else:
            for x in range(self.y):
                print()
            for i in range(self.height):
                for y in range(self.x):
                    print(" ", end="")
                for m in range(self.width):
                    print("#", end="")
                print()

    def __str__(self):
        """Returns informal representation of a rectangle"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for n in kwargs.keys():
                if n == "id":
                    self.id = kwargs['id']
                if n == "width":
                    self.width = kwargs['width']
                if n == "height":
                    self.height = kwargs['height']
                if n == "x":
                    self.x = kwargs['x']
                if n == "y":
                    self.y = kwargs['y']
