#!/usr/bin/python3
"""
Module that defines a function to list all attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: List of strings representing attribute and method names.
    """
    return dir(obj)
