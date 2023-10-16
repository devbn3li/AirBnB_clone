#!/usr/bin/python3
"""Contains the definition of FileStorage Class.
"""
import json


class FileStorage:
    """Handles serialization and deserialization of instances to/from JSON."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects currently in storage.

        Returns:
            dict: A dictionary with object IDs as keys and objects as values.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to storage.

        Args:
            obj: The object to add to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects in storage and saves them to a JSON file.
        """
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserializes objects from a JSON file and loads them into storage.
        If the JSON file does not exist, no exception is raised.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                obj_data = value
                class_name = key.split('.')[0]
                obj_instance = eval(class_name)(**obj_data)
                self.new(obj_instance)
        except FileNotFoundError:
            pass
