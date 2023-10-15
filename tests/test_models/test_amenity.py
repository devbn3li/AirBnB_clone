#!/usr/bin/python3
"""Unittest for Amenity
"""

import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """unittest_Amenity"""

    def test_attrib(self):
        """test for Amenity attribute"""

        my_amenity = Amenity()

        self.assertEqual(my_amenity.name, '')


if __name__ == '__main__':
    unittest.main()
