<<<<<<< HEAD
=======
#!/usr/bin/python3
"""
Review class inheriting from BaseModel
"""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """A class representing a review."""

    def __init__(self, *args, **kwargs):
        """Initialize the Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
=======
    """Defining public class attributes
    """
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
