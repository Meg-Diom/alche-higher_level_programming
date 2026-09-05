#!/usr/bin/python3
"""Defines a class ,MyList that inherits from list"""


class MyList(list):
    """Defining the class with a method"""


    def print_sorted(self):
        """Defining the instance method"""
        print(sorted(self))
