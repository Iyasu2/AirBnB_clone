#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_inheritance(self):
        """Test City inheritance from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test presence of attributes"""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))

    def test_attribute_types(self):
        """Test attribute types"""
        c = City()
        self.assertEqual(type(c.state_id), str)
        self.assertEqual(type(c.name), str)

    def test_attribute_values(self):
        """Test default attribute values"""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


if __name__ == "__main__":
    unittest.main()
