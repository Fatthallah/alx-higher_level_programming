#!/usr/bin/python3
"""t"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """h"""
    def __init__(self, size):
        """u"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

