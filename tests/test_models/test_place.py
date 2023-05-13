import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_attributes(self):
        """Test the default attributes of the Place instance."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_initialization(self):
        """Test the initialization of the Place instance."""
        place = Place(
            city_id="1",
            user_id="2",
            name="Cozy Apartment",
            description="A cozy place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=40.7128,
            longitude=-74.0060,
            amenity_ids=["1", "2"],
        )
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A cozy place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["1", "2"])

    def test_str_representation(self):
        """Test the __str__ method of the Place instance."""
        place = Place(name="Luxury Villa", price_by_night=500)
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of the Place instance."""
        place = Place(name="Cabin", price_by_night=200)
        place_dict = place.to_dict()

        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["created_at"], place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], place.updated_at.isoformat())
        self.assertEqual(place_dict["city_id"], "")
        self.assertEqual(place_dict["user_id"], "")
        self.assertEqual(place_dict["name"], "Cabin")
        self.assertEqual(place_dict["description"], "")
        self.assertEqual(place_dict["number_rooms"], 0)
        self.assertEqual(place_dict["number_bathrooms"], 0)
        self.assertEqual(place_dict["max_guest"], 0)
        self.assertEqual(place_dict["price_by_night"], 200)
        self.assertEqual(place_dict["latitude"], 0.0)
        self.assertEqual(place_dict["longitude"], 0.0)
        self.assertEqual(place_dict["amenity_ids"], [])

    def test_save_method(self):
        """Test the save method of the Place instance."""
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        updated_updated_at = place.updated_at

        self.assertNotEqual(original_updated_at, updated_updated_at)


if __name__ == "__main__":
    unittest.main()
