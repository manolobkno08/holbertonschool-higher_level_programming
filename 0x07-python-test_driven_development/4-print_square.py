#!/usr/bin/python3
"""
Function that print a square

Doctest check the tests

Always success
"""


def print_square(size):
    """Validate square"""
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for row in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print()


print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
