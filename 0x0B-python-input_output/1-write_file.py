#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Writes a string to a file UTF-8"""

    with open(filename, "w", encoding="utf-8") as f:
        r = f.write(text)
    
    return r