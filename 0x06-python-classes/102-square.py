#!/usr/bin/python3
"""XYZ"""

class Square:
    """XYZ"""

    def __init__(self, size=0):
        """XYZ"""
        self.__size = size

    @property
    def size(self):
        """XYZ"""
        return self.__size

    @size.setter
    def size(self, value):
        """XYZ"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """XYZ"""
        return self.__size**2

    def __eq__(self, o):
        """XYZ"""
        return self.__size == o.__size

    def __ne__(self, o):
        """XYZ"""
        return self.__size != o.__size

    def __gt__(self, o):
        """XYZ"""
        return self.__size > o.__size

    def __ge__(self, o):
        """XYZ"""
        return self.__size >= o.__size

    def __lt__(self, o):
        """XYZ"""
        return self.__size < o.__size

    def __le__(self, o):
        """XYZ"""
        return self.__size <= o.__size
