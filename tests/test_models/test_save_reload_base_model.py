import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestSaveReloadBaseModel(unittest.TestCase):
    """Test cases for the save and reload methods of BaseModel."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test environment."""
        storage.delete_all()

    def test_save_method(self):
        """Test the save method updates the updated_at attribute and saves the instance."""
        original_updated_at = self.model.updated_at
        self.model.save()
        updated_updated_at = self.model.updated_at

        self.assertNotEqual(original_updated_at, updated_updated_at)
        self.assertTrue(self.model.id in storage.all())

    def test_reload_method(self):
        """Test the reload method reloads the previously saved instance."""
        self.model.save()
        model_id = self.model.id
        storage.delete(self.model)

        self.assertNotIn(model_id, storage.all())

        storage.reload()
        reloaded_model = storage.get(BaseModel, model_id)

        self.assertIsNotNone(reloaded_model)
        self.assertEqual(reloaded_model.id, self.model.id)
        self.assertEqual(reloaded_model.created_at, self.model.created_at)
        self.assertEqual(reloaded_model.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
