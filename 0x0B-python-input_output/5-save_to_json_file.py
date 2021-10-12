#!/usr/bin/python3
"""
Write and return a Json object in a new file
"""
import json


def save_to_json_file(my_obj, filename):
    """Return new Json file"""
    with open(filename, "w") as jsonFile:
        return json.dump(my_obj, jsonFile)
