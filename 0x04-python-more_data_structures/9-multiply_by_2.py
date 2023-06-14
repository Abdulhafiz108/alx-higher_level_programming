#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new = list(a_dictionary.keys())
    tel = {}
    for i in new:
        tel[i] = 2 * a_dictionary.get(i)
    return tel
