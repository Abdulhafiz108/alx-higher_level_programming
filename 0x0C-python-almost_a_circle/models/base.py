#!/usr/bin/python3
"""Defines a base model class."""
import json
from rectangle import Rectangle

class Base:
    """Base model.

    It represents the base for all other classes in the project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file = cls.__name__ + ".json"
        with open(file, 'w', encoding = "utf-8") as jsonfile:
            if list_objs is not None:
                list_dict = [Rectangle.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_objs))
            else:
                jsonfile.write("[]")
