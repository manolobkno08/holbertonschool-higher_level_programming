#!/usr/bin/python3
"""Return sorted list"""


class MyList(list):
    """Return sorted list"""

    def __init__(self):
        self.list = []

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
