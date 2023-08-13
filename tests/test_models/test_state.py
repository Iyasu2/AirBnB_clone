#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_inheritance(self):
        """Test State inheritance from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test presence and defaults of attributes"""
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

    def test_attribute_types(self):
        """Test attribute types"""
        s = State()
        self.assertIsInstance(s.name, str)

    def test_instantiation(self):
        """Test instantiation of State"""
        self.assertEqual(State, type(State()))


if __name__ == "__main__":
    unittest.main()
