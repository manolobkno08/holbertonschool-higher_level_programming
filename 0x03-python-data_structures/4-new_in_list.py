#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpstr = my_list
    if idx < 0 or idx >= len(my_list):
        return cpstr
    cpstr = my_list[:]
    cpstr[idx] = element
    return cpstr
