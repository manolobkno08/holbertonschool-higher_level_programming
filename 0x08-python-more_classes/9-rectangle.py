#!/usr/bin/python3
"""Create new class"""


class Rectangle:

    """Create new entry point for rectangle and initialize"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """Return a string representation"""

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            pass
        else:
            string += '\n'.join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    """Return a repr"""

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    """Delete a rectangle"""

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """Return the biggest rectangle"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
