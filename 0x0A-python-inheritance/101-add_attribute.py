#!/usr/bin/python3
"""k"""
def add_attribute(obj, att, value):
    """k"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

