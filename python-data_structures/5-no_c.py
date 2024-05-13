#!/usr/bin/python3
def no_c(my_string):
    list_1 = ['c', 'C']

    new_str = my_string[:]
    new_str = "".join(i for i in my_string if i not in list_1)

    return new_str
