#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_copy = a_dictionary.copy()
    for i, j in new_copy.items():
        new_copy[i] = j * 2
    return new_copy
