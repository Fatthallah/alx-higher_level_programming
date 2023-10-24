#!/usr/bin/python3
"""XYZ"""
import math

class MagicClass:
    """XYZ"""

    def __init__(self, radius=0):
        """XYZ"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """XYZ"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """XYZ"""
        return (2 * math.pi * self.__radius)

