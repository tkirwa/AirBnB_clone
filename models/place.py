<<<<<<< HEAD
=======
#!/usr/bin/python3
"""
Class Place inheriting from BaseModel
"""
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """A class representing a place."""

    def __init__(self, *args, **kwargs):
        """Initialize the Place instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def __str__(self):
        """Return the string representation of the Place instance."""
        return "[Place] ({}) {}".format(self.id, self.__dict__)
=======
    """Defining public class attributes
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
>>>>>>> 4157f1142c53c8a5f10c3c863280090d635f4fc5
