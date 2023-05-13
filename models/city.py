<<<<<<< HEAD
=======
#!/usr/bin/python3
"""
City Class inheriting from BaseModel
"""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
    """A class representing a city."""

    def __init__(self, *args, **kwargs):
        """Initialize the City instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """Return the string representation of the City instance."""
        return "[City] ({}) {}".format(self.id, self.__dict__)
=======
    """Defining public class attributes
    """
    state_id = ""
    name = ""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
