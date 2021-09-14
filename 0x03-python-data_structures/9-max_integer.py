def max_integer(my_list=[]):
    long = len(my_list)
    my_list.sort()
    if long > 0:
        return my_list[-1]
    else:
        return None
