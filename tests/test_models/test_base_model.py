#!/usr/bin/python3
"""Unittest for BaseModel"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest_BaseModel"""

    def test_types(self):
        """test for types"""

        objects = BaseModel()
        objects.name = "My First Model"
        objects.my_number = 89
        self.assertEqual(objects.name, "My First Model")
        self.assertEqual(objects.my_number, 89)
        self.assertIsInstance(objects.id, str)
        self.assertIsInstance(objects.updated_at, datetime)
        self.assertIsInstance(objects.created_at, datetime)
        self.assertIsInstance(objects.name, str)
        self.assertIsInstance(objects.__class__.__name__, str)
        self.assertEqual(objects.__class__.__name__, 'BaseModel')
        self.assertIsInstance(objects.my_number, int)
        pr = f"[{objects.__class__.__name__}] ({objects.id}) {objects.__dict__}"
        self.assertEqual(str(objects), pr)

        obj_json = objects.to_dict()

        self.assertEqual(obj_json['name'], "My First Model")
        self.assertEqual(obj_json['my_number'], 89)
        self.assertIsInstance(obj_json['id'], str)
        self.assertIsInstance(obj_json['updated_at'], str)
        self.assertIsInstance(obj_json['created_at'], str)
        self.assertIsInstance(obj_json['name'], str)
        self.assertIsInstance(obj_json['__class__'], str)
        self.assertEqual(obj_json['__class__'], 'BaseModel')
        self.assertIsInstance(obj_json['my_number'], int)
        self.assertIsInstance(obj_json, dict)
        self.assertEqual
        (obj_json['updated_at'], datetime.isoformat(objects.updated_at))
        self.assertEqual
        (obj_json['created_at'], datetime.isoformat(objects.created_at))

        update_time = objects.updated_at

        objects.save()

        update_time2 = objects.updated_at
        self.assertNotEqual(update_time, update_time2)

        self.assertNotEqual(objects.updated_at, objects.created_at)

        obj2 = BaseModel()
        self.assertNotEqual(objects.id, obj2.id)
        self.assertNotEqual(objects, obj2)


if __name__ == '__main__':
    unittest.main()
