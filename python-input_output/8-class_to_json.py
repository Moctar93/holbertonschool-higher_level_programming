#!/usr/bin/python3
"""Module containing class_to_json() function
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Agrs:
        obj: (MyClass) object
    Return:
        (dict): dictionary
    """
    return obj.__dict__
