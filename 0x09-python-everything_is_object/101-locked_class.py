#!/usr/bin/python3
class LockedClass:
    """Prevent create new instances"""
    __slots__ = ['first_name']
