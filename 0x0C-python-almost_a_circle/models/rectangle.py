#!/usr/bin/python3
"""Rectangle module"""


from models.base import Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization"""
        super().__init__(id)
        self.validator("width", width)
        self.validator("height", height)
        self.xy_validator("x", x)
        self.xy_validator("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self.xy_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self.xy_validator("y", value)
        self.__y = value

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

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
