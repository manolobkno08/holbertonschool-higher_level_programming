#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    sum = 0
    for i in unique:
        sum = sum + i
    return sum
