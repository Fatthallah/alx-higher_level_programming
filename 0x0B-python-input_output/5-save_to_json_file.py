#!/usr/bin/python3
"""g"""
import json
def save_to_json_file(my_obj, filename):
    """q"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

