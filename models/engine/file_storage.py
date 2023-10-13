#!/usr/bin/python3

from models.base_model import BaseModel
from json import dump, load

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            dump(serialized_objs, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                obj_data = value
                obj_instance = eval(class_name)(**obj_data)
                self.new(obj_instance)
        except FileNotFoundError:
            pass
