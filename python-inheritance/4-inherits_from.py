#!/usr/bin/python3

"""
Module with a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    return (isinstance(obj, a_class) and type(obj) is not a_class)
