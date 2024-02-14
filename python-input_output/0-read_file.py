#!/usr/bin/python3
"""
This module contains a function for reading
and printing the contents of a file.
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
