#!/usr/bin/python3
"""
Returns a python object from Json string
"""
import json


def from_json_string(my_str):
    """Return python representation from Json string"""
    return json.loads(my_str)
