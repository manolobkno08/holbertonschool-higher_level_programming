#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    large = len(my_list)
    if idx > large or idx < 0:
        return my_list

    del my_list[idx]

    return my_list
