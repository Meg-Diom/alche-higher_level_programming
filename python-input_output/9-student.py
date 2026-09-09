#!/usr/bin/python3
"""Creating a module with a class Student"""


class Student:
    """Defining the class student"""

    def __init__(self, first_name, last_name, age):
        """Initializing the instant attribbutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Defining an instant method"""
        return obj.__dict__
