#!/usr/bin/python3
"""Module that defines a Square class with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class with area and string representation."""

    def __init__(self, size):
        """Initializes the square with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Returns a string description of the square.

        Returns:
            str: The square description in format [Square] size/size.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
