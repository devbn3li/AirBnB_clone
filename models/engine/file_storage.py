#!/usr/bin/python3
"""Contains the definition of FileStorage Class.
"""
from json import dump, load
from models.base_model import BaseModel


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to storage.

        Args:
            obj: The object to add to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects in storage and saves them to a JSON file.
        """
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            dump(serialized_objs, file)

    def reload(self):
        """
        Deserializes objects from a JSON file and loads them into storage.
        If the JSON file does not exist, no exception is raised.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                obj_data = value
                obj_instance = BaseModel(**obj_data)
                self.new(obj_instance)
        except FileNotFoundError:
            pass
