#!/usr/bin/python3

"""
Return the dictionary description for the json serialization.
"""


def class_to_json(obj):
    """Return the dictionary description"""
    return obj.__dict__
