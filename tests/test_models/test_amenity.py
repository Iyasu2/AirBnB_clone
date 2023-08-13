#!/usr/bin/python3
"""
Test module for Amenity class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test class for Amenity model"""

    def test_amenity_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attributes(self):
        """Test that Amenity has the required attributes"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))


if __name__ == "__main__":
    unittest.main()
