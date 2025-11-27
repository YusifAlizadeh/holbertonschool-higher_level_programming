#!/usr/bin/python3
"""Module providing a function to read and print a text file."""


def read_file(filename=""):
    """
    Read and print the contents of a UTF-8 text file.

    Parameters
    ----------
    filename : str
        Path to the text file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
