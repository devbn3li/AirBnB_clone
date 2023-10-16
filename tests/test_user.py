#!/usr/bin/python3
"""Unittest for User
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """unittest_User"""

    def test_attributes(self):
        """test for User attributes"""

        my_model = User()

        self.assertEqual(my_model.email, '')
        self.assertEqual(my_model.password, '')
        self.assertEqual(my_model.first_name, '')
        self.assertEqual(my_model.last_name, '')

if __name__ == '__main__':
    unittest.main()
