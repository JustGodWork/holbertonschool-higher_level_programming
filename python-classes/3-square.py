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

    def my_print(self):
        """Prints the square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
                pass
            pass
        pass

    @property
    def size(self):
        """Getter for size"""
        return self.__size
