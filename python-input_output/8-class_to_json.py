#!/usr/bin/python3
"""Utility for converting an object's attributes into a JSON-friendly dict."""


def class_to_json(obj):
    """Return a dictionary containing all attributes of an object."""
    return obj.__dict__.copy()
