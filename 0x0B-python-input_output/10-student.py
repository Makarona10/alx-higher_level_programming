#!/usr/bin/python3
"""Student module"""


class Student:
    """A student class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialises Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """returns a dictionary representation of Student"""
        if attr is not None:
            res = {i: self.__dict__[i] for i in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__