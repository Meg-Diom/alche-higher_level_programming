#!/usr/bin/python3
"""Function that returns the dictionary description of an object."""


def class_to_json(obj):
    """Defining the function"""
    return obj.__dict__
