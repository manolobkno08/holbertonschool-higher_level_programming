#!/usr/bin/python3

"""
Script that append all arguments and create a new file
"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

save_to_json_file(my_list + argv[1:], filename)
