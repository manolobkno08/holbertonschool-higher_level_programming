#!/usr/bin/python3
class LockedClass:
    """Onlyreate the instance attribute 'first_name'"""
    __slots__ = ['first_name']
