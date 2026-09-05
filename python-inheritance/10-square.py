#!/usr/bin/python3
"""Module ddefinition of class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition"""
    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self, size)

    def area(self):
        """public instance method"""
        return self.__size ** 2
