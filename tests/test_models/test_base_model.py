#!/usr/bin/python3
"""Unittest for BaseModel
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """unittest_BaseModel"""

    def test_type(self):
        """test type"""

        object = BaseModel()
        object.name = "ALX model"
        object.my_number = 89
        self.assertEqual(object.name, "ALX model")
        self.assertEqual(object.my_number, 89)


if __name__ == '__main__':
    unittest.main()
