#!/usr/bin/python3
"""Unittest for Place"""

import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """unittest_Place"""

    def test_attributes(self):
        """test Place attribute"""

        my_place = Place()

        self.assertEqual(my_place.city_id, '')
        self.assertEqual(my_place.user_id, '')
        self.assertEqual(my_place.name, '')
        self.assertEqual(my_place.description, '')
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
