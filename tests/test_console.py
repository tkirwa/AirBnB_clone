import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test the quit command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test the help command."""
        with patch('builtins.input', return_value='help'):
            HBNBCommand().cmdloop()
            self.assertIn(
                    "Documented commands (type help <topic>):",
                    mock_stdout.getvalue()
                    )

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test the emptyline method."""
        with patch('builtins.input', return_value=''):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "")

    # Add more test methods as needed


if __name__ == '__main__':
    unittest.main()
