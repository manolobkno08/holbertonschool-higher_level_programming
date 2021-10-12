#!/usr/bin/python3
"""
Function that read a text file
"""


def read_file(filename=""):
    """Read specified file"""
    with open(filename, encoding='utf-8') as f:
        return f.read()
