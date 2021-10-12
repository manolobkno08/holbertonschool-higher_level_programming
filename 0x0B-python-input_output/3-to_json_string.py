#!/usr/bin/python3
"""
Returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Return obj representation of JSON"""
    return json.dumps(my_obj)
