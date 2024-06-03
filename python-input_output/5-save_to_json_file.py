#!/usr/bin/python3
"""
    Write a function that writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    
    Args:
        my_obj: The object to be serialized to JSON.
        filename: The name of the file to save the JSON representation to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
