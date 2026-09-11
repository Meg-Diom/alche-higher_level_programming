#!/usr/bin/python3
"""Creating a Student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student"""
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces attributes with values from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)

