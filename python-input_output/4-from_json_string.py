#!/usr/bin/python3
"""Converting a JSON string into a Python object."""

import json


def from_json_string(my_str):
    """Defining a functio to convert to python"""
    return json.loads(my_str)
