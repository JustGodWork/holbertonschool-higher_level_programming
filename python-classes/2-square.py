#!/usr/bin/python3
class Square:
    """A class to represent a square"""
    def __init__(self, size=0):
        """Initializes the class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
