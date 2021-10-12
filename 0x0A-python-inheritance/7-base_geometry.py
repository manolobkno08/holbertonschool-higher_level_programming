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
