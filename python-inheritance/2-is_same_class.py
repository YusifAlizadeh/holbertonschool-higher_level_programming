#!/usr/bin/python3
"""
This module provides a function to determine whether an object is
exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if `obj` is exactly an instance of `a_class`,
    otherwise return False.

    Parameters:
        obj: any Python object
        a_class: the class to compare the object's exact type to

    Returns:
        bool: True if `type(obj) is a_class`, False otherwise
    """
    return type(obj) is a_class
