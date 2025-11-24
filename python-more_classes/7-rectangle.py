#!/usr/bin/python3
"""
This module defines a Rectangle class with:
- Width and height validation
- Area and perimeter methods
- String and recreatable representations
- Class attributes for number of instances and print symbol
- Deletion detection
"""


class Rectangle:
    """
    Represents a rectangle with width and height validation.
    Tracks number of instances and allows customizable string representation.
    """

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle with optional width and height.

        Args:
            width (int): Rectangle width (default 0)
            height (int): Rectangle height (default 0)

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is negative
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle printed with print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        # Convert the symbol to string for printing
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string representation to recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the instance is deleted and update counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
