#!/usr/bin/python3
"""
Return a python object from Json File
"""
import json


def load_from_json_file(filename):
    """Return new python obj"""
    with open(filename) as f:
        return json.load(f)
