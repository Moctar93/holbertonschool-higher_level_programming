#!/usr/bin/python3
"""
    A subclass of list with a method to print the list in sorted order
    Prints the list in ascending order.
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
