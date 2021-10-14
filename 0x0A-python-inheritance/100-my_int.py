#!/usr/bin/python3
"""
My Class
"""


class MyInt(int):
    """My Int Class"""

    def __eq__(self, other):
        return isinstance(other, MyInt)

    def __ne__(self, other):
        return not isinstance(other, MyInt)
