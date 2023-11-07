#!/usr/bin/python3
"""y"""
def append_write(filename="", text=""):
    """qqq"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

