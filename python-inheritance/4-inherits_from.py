#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
