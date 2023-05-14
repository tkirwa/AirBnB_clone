#!/usr/bin/python3
"""
This module contains unit tests for the FileStorage class.
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test suite for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up test environment.
        """
        del self.storage

    def test_all(self):
        """
        Test the all() method of FileStorage.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Add the instance to the storage
        self.storage.new(model)
        # Retrieve all objects from the storage
        objects = self.storage.all()
        # Assert that the objects dictionary contains the BaseModel instance
        self.assertIn("BaseModel.{}".format(model.id), objects)

    def test_new(self):
        """
        Test the new() method of FileStorage.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Add the instance to the storage
        self.storage.new(model)
        # Retrieve all objects from the storage
        objects = self.storage.all()
        # Assert that the objects dictionary contains the BaseModel instance
        self.assertIn("BaseModel.{}".format(model.id), objects)

    def test_save_reload(self):
        """
        Test the save() and reload() methods of FileStorage.
        """
        # Create a new BaseModel instance
        model = BaseModel()
        # Add the instance to the storage
        self.storage.new(model)
        # Save the storage to a file
        self.storage.save()
        # Clear the storage
        del self.storage
        # Create a new storage
        self.storage = FileStorage()
        # Reload the storage from the file
        self.storage.reload()
        # Retrieve all objects from the storage
        objects = self.storage.all()
        # Assert that the objects dictionary contains the BaseModel instance
        self.assertIn("BaseModel.{}".format(model.id), objects)


if __name__ == "__main__":
    unittest.main()
