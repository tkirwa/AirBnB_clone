<<<<<<< HEAD
=======
#!/usr/bin/python3
"""
Class Amenity inheriting from BaseModel
"""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
from models.base_model import BaseModel


class Amenity(BaseModel):
<<<<<<< HEAD
    """A class representing an amenity."""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
=======
    """Defining public class attributes
    """
    name = ""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
