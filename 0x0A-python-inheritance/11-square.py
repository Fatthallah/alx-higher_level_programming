#!/usr/bin/python3
"""y"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """y"""
    def __init__(self, size):
        """k"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

