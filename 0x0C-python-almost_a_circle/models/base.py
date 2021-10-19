#!/usr/bin/python3
"""
Create new class Base
"""

import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance"""
        if cls.__name__ == "Square":
            dummy = cls(8)
        elif cls.__name__ == "Rectangle":
            dummy = cls(8, 8)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """List Instance"""
        final_list = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                object_list = cls.from_json_string(f.read())
                for object in object_list:
                    final_list.append(cls.create(**object))
            return final_list
