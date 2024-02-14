#!/usr/bin/python3
"""
This module defines a function called "lookup" that takes an object
as an argument and provides a list of its attributes and methods.
"""


def lookup(obj):
    """
    Return list of available attributes and methods of an object.

    Function uses built-in dir() method to return a list of valid
    attributes and methods of passed object. It is useful for introspection
    to understand what operations can be performed on the object.

    Args:
        obj (Any): The object for introspection.

    Returns:
        list: A list of string names of the object's attributes and methods.
    """
    return dir(obj)
