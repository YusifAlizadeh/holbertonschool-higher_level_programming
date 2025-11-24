#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list
and adds a method to print the list sorted.
"""


class MyList(list):
    """Represents a list with a method to print it sorted."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
