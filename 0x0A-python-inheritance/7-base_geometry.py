#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """A class with public attribute area"""


    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """that validates value"""

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))