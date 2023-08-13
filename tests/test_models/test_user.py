#!/usr/bin/python3
"""Unittests for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test presence and defaults of attributes"""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_attribute_types(self):
        """Test attribute types"""
        u = User()
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)

    def test_instantiation(self):
        """Test instantiation of User class"""
        self.assertEqual(User, type(User()))


if __name__ == "__main__":
    unittest.main()
