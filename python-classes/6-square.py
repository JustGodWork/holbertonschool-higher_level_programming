#!/usr/bin/python3
"""A module that defines a square."""


class Square:
    """A class to represent a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if not self.size:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
