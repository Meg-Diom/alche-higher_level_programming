#!/usr/bin/python3
"""Reading files in python"""


def read_file(filename=""):
    """Defining a function that takes a file nane as input and reads the file"""
    with open("filename", "r", encoding="utf-8") as file:
        print(file.read(), end=")
