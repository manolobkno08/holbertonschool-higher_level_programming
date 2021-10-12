#!/usr/bin/python3
"""Return sorted list"""


class MyList(list):
    """Return sorted list"""

    def __init__(self):
        self.list = []

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
