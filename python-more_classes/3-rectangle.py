#!/usr/bin/python3
"""Defining the class Rectangle"""


class Rectangle:
    """Creating the class rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Creating a public instance method, area"""
        return self.__width * self.__height

    def perimeter(self):
        """Creating a public instance method, perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimtr = 0
        else:
            perimtr = (self.__width + self.__height) * 2
        return perimtr

    def __str__(self):
        """printing the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

    rows = []
    for i in range(self.__height):
        rows.append("#" * self.__width)
    return "\n".join(rows)
