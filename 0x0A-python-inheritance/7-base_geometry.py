#!/usr/bin/python3
"""x"""
class BaseGeometry:
    """x"""
    def area(self):
        """x"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """x"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

