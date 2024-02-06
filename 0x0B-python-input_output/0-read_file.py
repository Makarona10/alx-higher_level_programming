#!/usr/bin/python3
"""Reading module"""

def read_file(filename=""):
    """
    Reads a file with UTF-8
    
    Args:
        filename: The file that will be read
    """
    with open(filename, "r", encoding='utf-8') as f:
        for i in f.readlines:
            print(i)