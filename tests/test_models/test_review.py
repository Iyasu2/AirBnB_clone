#!/usr/bin/python3
"""Unittests for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test presence and defaults of attributes"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))

        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_attribute_types(self):
        """Test attribute types"""
        r = Review()
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)

    def test_instantiation(self):
        """Test instantiation of Review class"""
        self.assertEqual(Review, type(Review()))


if __name__ == "__main__":
    unittest.main()
