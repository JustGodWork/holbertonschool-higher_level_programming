#!/usr/bin/python3
"""Module for print_square function."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size of the square.

    Returns:
        None.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
