#!/usr/bin/python3
"""Create new class"""


class Rectangle:
    """Create new entry point for rectangle and initialize"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Get property to width"""
    @property
    def width(self):
        return self.__width

    """Set property to width"""
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    """Get property to height"""
    @property
    def height(self):
        return self.__height

    """Set property to height"""
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    """Create a new method that return the area"""

    def area(self):
        return self.__height * self.__width

    """Create a new method that return the area"""

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2*self.__height) + (2*self.__width))
