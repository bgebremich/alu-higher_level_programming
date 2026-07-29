#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initializes the square with a given size.

        Args:
            size: The size of the square.
        """
        self.__size = size
