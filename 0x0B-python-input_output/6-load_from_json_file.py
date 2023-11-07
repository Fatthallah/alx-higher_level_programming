#!/usr/bin/python3
"""u"""
import json
def load_from_json_file(filename):
    """k"""
    with open(filename) as f:
        return json.load(f)

