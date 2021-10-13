#!/usr/bin/python3

"""
Class that defines a Student
"""


class Student():
    """Define Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for row in attrs:
                if row in self.__dict__.keys():
                    new_dict[row] = self.__dict__[row]
            return new_dict
