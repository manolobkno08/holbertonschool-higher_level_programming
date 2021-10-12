#!/usr/bin/python3
"""
Function that append new string
"""


def append_write(filename="", text=""):
    """Create or append new string at the final of a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
