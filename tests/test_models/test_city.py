import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up test environment."""
        self.city = City()

    def test_attributes(self):
        """Test the default attributes of the City instance."""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_initialization(self):
        """Test the initialization of City instance."""
        city = City(name="New York", state_id="NY")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "NY")

    def test_str_representation(self):
        """Test the __str__ method of the City instance."""
        city = City(name="Los Angeles", state_id="CA")
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of the City instance."""
        city = City(name="Chicago", state_id="IL")
        city_dict = city.to_dict()

        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())
        self.assertEqual(city_dict["name"], "Chicago")
        self.assertEqual(city_dict["state_id"], "IL")

    def test_save_method(self):
        """Test the save method of the City instance."""
        original_updated_at = self.city.updated_at
        self.city.save()
        updated_updated_at = self.city.updated_at

        self.assertNotEqual(original_updated_at, updated_updated_at)

    def test_reload_method(self):
        """Test the reload method of the City instance."""
        self.city.save()
        city_id = self.city.id
        city_copy = City()
        city_copy.reload()

        self.assertEqual(city_copy.id, city_id)
        self.assertEqual(city_copy.created_at, self.city.created_at)
        self.assertEqual(city_copy.updated_at, self.city.updated_at)


if __name__ == "__main__":
    unittest.main()
