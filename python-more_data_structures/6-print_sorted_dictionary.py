#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    diction_keys = list(a_dictionary.keys())
    diction_keys.sort()
    for i in diction_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
