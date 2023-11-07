#!/usr/bin/python3
"""h"""
class Student:
    """t"""
    def __init__(self, first_name, last_name, age):
        """u"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """e"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
    def reload_from_json(self, json):
        """k"""
        for k, v in json.items():
            setattr(self, k, v)

