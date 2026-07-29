#!/usr/bin/python3
"""Module that defines a to_json_string function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
