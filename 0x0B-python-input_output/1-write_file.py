#!/usr/bin/python3
"""
Function that write and return the length of file
"""


def write_file(filename="", text=""):
    """Create or overwrite a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
