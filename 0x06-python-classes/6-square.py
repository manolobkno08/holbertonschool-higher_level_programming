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
        if type(position) is not tuple or type(position[0]) is not int\
                or type(position[1]) is not int or position[0] < 0\
                or position[1] < 0 or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for it_1 in range(self.__position[0])]), end="")
            print("".join(["#" for it_2 in range(self.__size)]))


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
