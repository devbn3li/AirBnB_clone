#!/usr/bin/python3
"""Unittest for User"""

import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """unittest_User"""

    def test_attrib(self):
        """test for User attributes"""

        model = User()

        self.assertEqual(model.email, '')
        self.assertEqual(model.password, '')
        self.assertEqual(model.first_name, '')
        self.assertEqual(model.last_name, '')


if __name__ == '__main__':
    unittest.main()
