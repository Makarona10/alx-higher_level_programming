#!/usr/bin/python3
"""appending module"""


def append_write(filename="", text=""):
    """appending function"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)