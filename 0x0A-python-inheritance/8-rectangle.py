#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """public method area"""

    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")

    """Validator"""

    def integer_validator(self, name, value):
        """Exception"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(value))


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
