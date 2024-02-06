#!/usr/bin/python3
import json
"""to json module"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)"""
    return json.dumps(repr(my_obj))