#!/usr/bin/python3
"""Creating a function that loads fron a json file"""


import json


def load_from_json_file(filename):
    """Defining the function"""
    with open(filename, "r", encoding="utf-8") as file:
        my_list = json.load(file)
        return my_list
