#!/usr/bin/python3

"""
This module contains a function that appends a string at the end of
a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
