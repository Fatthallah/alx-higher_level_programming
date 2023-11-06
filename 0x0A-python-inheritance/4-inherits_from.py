#!/usr/bin/python3
"""x"""
def inherits_from(obj, a_class):
    """x"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

