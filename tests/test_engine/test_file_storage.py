#!/usr/bin/python3
"""Unittest for BaseModel class"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """unittest for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment"""
        del self.storage

    def test_all(self):
        """Test all method"""

        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method"""

        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""

        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            self.assertIn(model.id, f.read())

    def test_reload(self):
        """Test reload method"""

        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
