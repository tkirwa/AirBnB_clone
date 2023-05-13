from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representing an amenity."""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
