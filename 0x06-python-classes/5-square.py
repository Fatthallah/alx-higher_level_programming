#!/usr/bin/python3
"""XYZ"""

class Square:
    """XYZ"""

    def __init__(self, size):
        """XYZ"""
        self.size = size

    @property
    def size(self):
        """XYZ"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """XYZ"""
        return (self.__size * self.__size)

    def my_print(self):
        """XYZ"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

