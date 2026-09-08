#!/usr/bin/python3
"""This module creates a file and writes into or overwrite the file"""


def write_file(filename="", text=""):
    """Defining the functiion that creates the file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
