#!/usr/bin/python3
"""Load from json file module"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""

    with open(filename, "r", encoding="utf-8") as f:
        myObject = json.load(f)
    return myObject