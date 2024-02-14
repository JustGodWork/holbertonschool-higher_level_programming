#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class and the `Rectangle` class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initializes a new Rectangle instance."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
