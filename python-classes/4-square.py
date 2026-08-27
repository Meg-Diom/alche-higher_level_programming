#!/usr/bin/python3
"""Defining a class Square that has getters and setters"""


class Square:
    """Defining the class"""
    def __init__(self, size=0):
        """Catching errors"""
        self.__size == size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defining the public instance method"""
        return self.__size ** 2
