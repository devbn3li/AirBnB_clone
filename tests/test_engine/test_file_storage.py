#!/usr/bin/python3
"""Unittest for BaseModel"""


import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """tests for file storage"""

    def test_storage(self):
        """test for storage"""

        self.assertTrue(isinstance(storage, FileStorage))
