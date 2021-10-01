#!/usr/bin/python3
"""Lock class"""


class LockedClass:
    """Only create the instance attribute 'first_name'"""
    __slots__ = ['first_name']
