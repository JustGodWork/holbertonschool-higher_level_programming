#!/usr/bin/python3
"""
This module defines a function called "lookup" that takes an object
as an argument and provides a list of its attributes and methods.
"""


def lookup(obj):
    return dir(obj)
