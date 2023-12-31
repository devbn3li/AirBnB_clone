#!/usr/bin/python3
"""Unittest for BaseModel class."""


import unittest
from datetime import datetime

from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """unittest BaseModel"""

    def test_storage(self):
        """test storage"""

        all_obj = storage.all()
        for obj_id in all_obj.keys():
            obj = all_obj[obj_id]

        try:
            with open("file.json", "r", encoding='utf-8') as f:
                self.assertIsInstance(all_obj, dict)
                self.assertIsInstance(obj, BaseModel)
                val = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
                self.assertEqual(str(obj), val)
                self.assertEqual(f"{obj_id}",
                                 f"{obj.__class__.__name__}.{obj.id}")
        except FileNotFoundError:
            self.assertIsInstance(all_obj, dict)
            self.assertEqual(all_obj, {})

        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        model.save()


if __name__ == '__main__':
    unittest.main()
