#!/usr/bin/python3
"""Creating a function to save object to file"""

import json


def save_to_json_file(my_obj, filename):
    """Defining the function"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, filename)
