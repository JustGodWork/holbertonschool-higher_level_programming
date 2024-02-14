#!/usr/bin/python3
"""
Module with a function to check if an object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is an instance of a_class.

    Args:
    obj -- the object to check
    a_class -- the reference class

    Returns:
    True if obj is an instance of a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is a_class
