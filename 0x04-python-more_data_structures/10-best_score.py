#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None
    new = list(a_dictionary.keys())
    a = new[0]
    for i in new:
        if a_dictionary.get(i) > a_dictionary.get(a):
            a = i
    return a
