#!/usr/bin/python3
"""Unittest for State
"""

import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """Class to test the State class
    """

    def test_attrib(self):
        """
        Test the attributes of the State class
        """

        my_state = State()

        self.assertTrue(my_state.name, '')
