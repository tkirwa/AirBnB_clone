import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def tearDown(self):
        self.console.reset()

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as f:
                self.console.onecmd(f"show BaseModel {obj_id}")
                output = f.getvalue().strip()
                self.assertIn(obj_id, output)

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as f:
                self.console.onecmd(f"destroy BaseModel {obj_id}")
                output = f.getvalue().strip()
                self.assertEqual(output, "")

    def test_update(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as f:
                self.console.onecmd(f"update BaseModel {obj_id} name 'New Name'")
                output = f.getvalue().strip()
                self.assertEqual(output, "")

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as f:
                self.console.onecmd("all BaseModel")
                output = f.getvalue().strip()
                self.assertIn(obj_id, output)

    def test_count(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            with patch("sys.stdout", new=StringIO()) as f:
                self.console.onecmd("count BaseModel")
                output = f.getvalue().strip()
                self.assertEqual(output, "1")

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")


if __name__ == "__main__":
    unittest.main()
