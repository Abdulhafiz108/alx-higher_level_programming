#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    cpy = [x for x in my_list]
    if idx > 0 and idx < len(my_list):
        cpy[idx] = element
    return cpy
