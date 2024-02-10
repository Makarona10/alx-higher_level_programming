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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json.dumps(list_dictionaries)
