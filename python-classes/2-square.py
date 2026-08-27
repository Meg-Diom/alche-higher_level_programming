#!/usr/bin/python3
"""Defining a class the catches errors"""


class Square:
    """Defining the class Square"""
    def __init__(self, size=0):
        """Initializing the method and raising errors"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

