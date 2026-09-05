#!/usr/bin/python3
"""Module Inintialization"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square"""

    def __init__(self, size):
        """Initializatin of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """public instance method"""
        return self.__size ** 2

    def __str__(self):
        """returning a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
