#!/usr/bin/python3
"""
    script that adds all arguments to a Python list
    and then save them to a file
"""


import sys
import os


# Importing the necessary functions from the provided modules
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Define the filename for storing the list
filename = "add_item.json"

# Initialize the list
try:
    # If the file exists, load the existing list
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
