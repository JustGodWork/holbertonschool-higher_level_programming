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

    def area(self):
        """Returns the area of the square"""
        return self.size * self.size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        pass
    pass
