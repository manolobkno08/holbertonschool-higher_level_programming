#!/usr/bin/python3
"""Square is a class"""


class Square():
    """Return private attribute"""

    def __init__(self, size=0):
        self.size = size

    """Define a new method"""

    def area(self):
        """Return square area"""
        return(self.__size ** 2)

    """Print a square #"""

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("".join('#' for i in range(self.size)))

    """New get property"""
    @property
    def size(self):
        """Get property"""
        return(self.__size)
    """New setter property"""
    @size.setter
    def size(self, size):
        """size must be an integer, otherwise raise a TypeError"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            """if size is less than 0, raise a ValueError"""
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                """Private instance attribute: size"""
                self.__size = size
