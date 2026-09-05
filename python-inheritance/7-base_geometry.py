#!/usr/bin/python3
"""Module that defines a class"""


class BaseGeometry:
    """Class definition"""
    def area(self):
        """Raising error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Error raising"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
