#!/usr/bin/python3
"""
This module defines a function that checks whether an object is an
instance of a specified class or a class inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if `obj` is an instance of `a_class` or a class that
    inherited from `a_class`. Otherwise return False.

    Parameters:
        obj: any Python object
        a_class: the class to check against

    Returns:
        bool: True if isinstance(obj, a_class), False otherwise
    """
    return isinstance(obj, a_class)
