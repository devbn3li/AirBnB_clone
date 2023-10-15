#!/usr/bin/python3
"""Unittest for Review"""

import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """unittest_Review"""

    def test_attributes(self):
        """test Review attribute"""

        my_review = Review()

        self.assertEqual(my_review.place_id, '')
        self.assertEqual(my_review.user_id, '')
        self.assertEqual(my_review.text, '')
