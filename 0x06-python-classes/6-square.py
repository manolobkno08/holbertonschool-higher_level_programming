#!/usr/bin/python3
"""Square is a class"""


class Square():
    """Return private attribute"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """Define get method"""
    @property
    def position(self):
        return(self.__position)

    """Define SET method and validations"""
    @position.setter
    def position(self, position):
        if self.check_tuple(position) is False \
           or self.check_indexes(position) is False \
           or self.check_integers(position) is False \
           or self.check_values(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def check_tuple(self, position):
        if type(position) is tuple:
            return True
        return False

    def check_indexes(self, position):
        if len(position) == 2:
            return True
        return False

    def check_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True
        return False

    def check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True
        return False

        """Define a new method"""

    def area(self):
        """Return square area"""
        return(self.__size ** 2)

    """Print a square #"""

    def my_print(self):
        """prints the square
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for it_1 in range(self.__position[0])]), end="")
            print("".join(["#" for it_2 in range(self.__size)]))


try:
    my_square = Square(3, (1, ))
except Exception as e:
    print(e)
