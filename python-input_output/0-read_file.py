#!/usr/bin/python3
"""
This module contains a function for reading
and printing the contents of a file.
"""


def read_file(filename=""):
    """Read a file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
