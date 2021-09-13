#!/usr/bin/puthon3
def new_in_list(my_list, idx, element):
    cpstr = my_list.copy()
    if idx < 0:
        return cpstr
    elif idx > len(my_list):
        return cpstr
    else:
        for i in range(len(cpstr)):
            if i == idx:
                cpstr[i] = element
                return cpstr
