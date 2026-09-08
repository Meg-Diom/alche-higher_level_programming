#!/usr/bin/python3
"""This module adds text to existing text without overwriting"""


def append_write(filename="", text=""):
    """Defining the appending function"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
