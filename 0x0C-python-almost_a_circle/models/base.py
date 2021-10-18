#!/usr/bin/python3
"""
Create new class Base
"""

import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiallize attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Create new JSON representation"""
        if list_dictionaries == [] or list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create new file with JSON representation"""
        filename = cls.__name__ + '.json'
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """Representation of Json to String"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
