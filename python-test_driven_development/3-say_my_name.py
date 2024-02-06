#!/usr/bin/python3
"""Module for say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Prints a name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        None.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
