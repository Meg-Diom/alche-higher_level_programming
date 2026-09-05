#!/usr/bin/python3
"""This module defines inherit_from"""


def inherits_from(obj, a_class):
    """This function takes s parameters"""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
