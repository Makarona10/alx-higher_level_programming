#!/usr/bin/python3
"""Class base module"""

import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def validator(self, var, val):
        """check on the value of height and width"""
        if type(val) is not int:
            raise TypeError('{} must be an integer'.format(var))
        if val <= 0:
            raise ValueError('{} must be > 0'.format(var))

    def xy_validator(self, var, val):
        """check on the value of x and y"""
        if type(val) is not int:
            raise TypeError('{} must be an integer'.format(var))
        if val < 0:
            raise ValueError('{} must be >= 0'.format(var))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(list_objs, cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                data = [i.to_dictionary() for i in list_objs]
                json_str = cls.to_json_string(data)
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []
