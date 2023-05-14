import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        """Test save method of BaseModel."""
        model = BaseModel()
        previous_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(previous_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel."""
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

    def test_str(self):
        """Test __str__ method of BaseModel."""
        model = BaseModel()
        model_str = str(model)
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model_str, expected_str)


if __name__ == '__main__':
    unittest.main()
