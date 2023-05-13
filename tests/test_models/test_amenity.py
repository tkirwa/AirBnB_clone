#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel



class TestAmenity(unittest.TestCase):
    """
    Test suite for the Amenity class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up test environment.
        """
        del self.amenity

    def test_inheritance(self):
        """
        Test that Amenity inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of Amenity.
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        """
        Test the __str__() method of Amenity.
        """
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)

    def test_to_dict(self):
        """
        Test the to_dict() method of Amenity.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_from_dict(self):
        """
        Test the from_dict() method of Amenity.
        """
        amenity_dict = {
            "__class__": "Amenity",
            "id": "123",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "name": "Wifi"
        }
        amenity = Amenity.from_dict(amenity_dict)
        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(amenity.updated_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(amenity.name, "Wifi")

if __name__ == "__main__":
    unittest.main()
