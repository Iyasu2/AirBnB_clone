#!/usr/bin/python3
"""
This module defines unit tests for the BaseModel class.
"""

import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a fresh instance of BaseModel for each test.
        """
        self.base_model = BaseModel()

    def test_id_is_uuid(self):
        """
        Test if the ID is a valid UUID.
        """
        self.assertTrue(isinstance(self.base_model.id, str))
        self.assertTrue(uuid.UUID(self.base_model.id))

    def test_created_at_and_updated_at(self):
        """
        Test the 'created_at' and 'updated_at' attributes.
        """
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """
        Test the save() method's behavior.
        """
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(
            self.base_model.updated_at, previous_updated_at,
            "Calling save() should update the updated_at attribute."
        )

    def test_to_dict_method(self):
        """
        Test the to_dict() method.
        """
        instance_dict = self.base_model.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')

    def test_from_dict_method(self):
        """
        Test the from_dict() method.
        """
        instance_dict = self.base_model.to_dict()
        new_instance = BaseModel.from_dict(instance_dict)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.id, self.base_model.id)
        self.assertEqual(new_instance.created_at, self.base_model.created_at)
        self.assertEqual(new_instance.updated_at, self.base_model.updated_at)

    def test_new_instance_has_id(self):
        """
        Test if a new instance has the 'id' attribute.
        """
        new_instance = BaseModel()
        self.assertTrue(hasattr(new_instance, 'id'))

    def test_new_instance_has_created_and_updated_at(self):
        """
        Test if a new instance has 'created_at' and 'updated_at' attributes.
        """
        new_instance = BaseModel()
        self.assertTrue(hasattr(new_instance, 'created_at'))
        self.assertTrue(hasattr(new_instance, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
