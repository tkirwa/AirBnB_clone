import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_attributes(self):
        """Test the default attributes of the State instance."""
        state = State()
        self.assertEqual(state.name, "")

    def test_initialization(self):
        """Test the initialization of State instance."""
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_str_representation(self):
        """Test the __str__ method of the State instance."""
        state = State(name="Texas")
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of the State instance."""
        state = State(name="New York")
        state_dict = state.to_dict()

        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["created_at"], state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], state.updated_at.isoformat())
        self.assertEqual(state_dict["name"], "New York")

    def test_save_method(self):
        """Test the save method of the State instance."""
        state = State()
        original_updated_at = state.updated_at
        state.save()
        updated_updated_at = state.updated_at

        self.assertNotEqual(original_updated_at, updated_updated_at)



if __name__ == '__main__':
    unittest.main()