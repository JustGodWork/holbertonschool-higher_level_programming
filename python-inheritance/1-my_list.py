#!/usr/bin/python3

"""
Defines a custom class which is a subclass of the built-in `list` class.
Method `print_sorted` to print the elements of the list in sorted order.
"""


class MyList(list):
    """Class which is a subclass of the built-in list class."""

    def print_sorted(self):
        print(sorted(self))
