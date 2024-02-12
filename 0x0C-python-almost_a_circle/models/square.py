#!/usr/bin/python3
"""The square module"""


Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    """The square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The square initialization"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns representation of the rectangle"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    @property
    def size(self):
        """The getter of a square size"""
        return self.width

    @size.setter
    def size(self, value):
        """The square size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle"""
        if len(args) != 0:
            attrs = ("id", "size", "x", "y")
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, val in kwargs.items():
                setattr(self, k, val)

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y}