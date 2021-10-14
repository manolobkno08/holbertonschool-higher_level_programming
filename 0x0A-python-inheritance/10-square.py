#!/usr/bin/python3
"""
Return Square
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))


s = Square(13)

print(s)
print(s.area())