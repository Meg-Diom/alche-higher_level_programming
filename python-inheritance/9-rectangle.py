#!/usr/bin/python3
"""Module defining class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining inheriting class"""

    def __init__(self, width, height):
        """initializing a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returning the rectsngle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
