#!/usr/bin/python3
"""
module of 1-write_file
"""


def write_file(filename="", text=""):
    """ 
    returns the number of lines of a text file
    """
    with open(filename, "w") as f:
        return f.write(str(text))
