#!/usr/bin/python3
"""Creating a class Student with instance attributes"""


class Student:
    """Defining class"""

    def __init__(self, first_name, last_name, age):
        """instantiating attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """definig instant methods"""
        if isinstance(attrs, list) 
        and all(isinstance(item, str) for item in attrs):
            return {
                key: self.__dict__[key] 
                for key in attrs 
                if key in self.__dict__}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Reloading from a JSON file"""
        for key, value in json.items():
            satattr(self, key, value)
