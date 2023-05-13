from models.base_model import BaseModel


class Place(BaseModel):
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
