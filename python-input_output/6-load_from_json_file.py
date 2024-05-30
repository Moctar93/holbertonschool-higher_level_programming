#!/usr/bin/python3
"""
    function that creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file to load.

        Returns:
        The object represented by the JSON data in the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
