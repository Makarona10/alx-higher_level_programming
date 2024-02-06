#!/usr/bin/python3
"""Reading module (readfile)"""


def read_file(filename=""):
    """Reads a file with UTF-8"""
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")