#!/usr/bin/python3
"""
    function that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
