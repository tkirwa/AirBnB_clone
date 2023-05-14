import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """Test cases for the to_dict method of BaseModel."""

    def test_to_dict(self):
        """Test conversion of BaseModel instance to dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(
                model_dict["created_at"],
                model.created_at.isoformat()
                )
        self.assertEqual(
                model_dict["updated_at"],
                model.updated_at.isoformat()
                )

    def test_to_dict_custom_attrs(self):
        """Test conversion of BaseModel
        instance with custom attributes to dictionary.
        """
        model = BaseModel()
        model.name = "Test Model"
        model.number = 12345
        model_dict = model.to_dict()

        self.assertIn("name", model_dict)
        self.assertIn("number", model_dict)
        self.assertEqual(model_dict["name"], "Test Model")
        self.assertEqual(model_dict["number"], 12345)

    def test_to_dict_nested_objects(self):
        """Test conversion of BaseModel instance
        with nested objects to dictionary.
        """
        model = BaseModel()
        nested_model = BaseModel()
        nested_model.name = "Nested Model"
        model.nested = nested_model
        model_dict = model.to_dict()

        self.assertIn("nested", model_dict)
        self.assertIsInstance(model_dict["nested"], dict)
        self.assertEqual(model_dict["nested"]["__class__"], "BaseModel")
        self.assertEqual(model_dict["nested"]["name"], "Nested Model")

    def test_to_dict_exclude_attributes(self):
        """Test conversion of BaseModel instance
        excluding specified attributes.
        """
        model = BaseModel()
        model.exclude = "This should be excluded"
        model_dict = model.to_dict(exclude=["exclude"])

        self.assertNotIn("exclude", model_dict)

    def test_to_dict_include_attributes(self):
        """Test conversion of BaseModel instance
        including specified attributes.
        """
        model = BaseModel()
        model.include = "This should be included"
        model_dict = model.to_dict(include=["include"])

        self.assertIn("include", model_dict)
        self.assertEqual(model_dict["include"], "This should be included")


if __name__ == '__main__':
    unittest.main()
