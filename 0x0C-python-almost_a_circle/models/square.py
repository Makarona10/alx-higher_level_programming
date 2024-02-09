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
