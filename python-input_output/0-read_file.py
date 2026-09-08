#!/usr/bin/python3
"""This module containe a function that reads files"""


def read_file(filename=""):
    """
    Defining a function that takes a file nane as input and reads the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
