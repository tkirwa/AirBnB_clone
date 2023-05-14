import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test environment."""
        self.user = User()

    def test_attributes(self):
        """Test the default attributes of the User instance."""
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")

    def test_initialization(self):
        """Test the initialization of User instance."""
        user = User(
                first_name="John",
                last_name="Doe",
                email="johndoe@example.com",
                password="password"
                )
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertEqual(user.password, "password")

    def test_str_representation(self):
        """Test the __str__ method of the User instance."""
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of the User instance."""
        user = User(
                first_name="John",
                last_name="Doe",
                email="johndoe@example.com",
                password="password"
                )
        user_dict = user.to_dict()

        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")
        self.assertEqual(user_dict["email"], "johndoe@example.com")
        self.assertEqual(user_dict["password"], "password")

    def test_save_method(self):
        """Test the save method of the User instance."""
        original_updated_at = self.user.updated_at
        self.user.save()
        updated_updated_at = self.user.updated_at

        self.assertNotEqual(original_updated_at, updated_updated_at)

    def test_reload_method(self):
        """Test the reload method of the User instance."""
        self.user.save()
        user_id = self.user.id
        user_copy = User()
        user_copy.reload()

        self.assertEqual(user_copy.id, user_id)
        self.assertEqual(user_copy.created_at, self.user.created_at)
        self.assertEqual(user_copy.updated_at, self.user.updated_at)


if __name__ == '__main__':
    unittest.main()
