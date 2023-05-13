from models.base_model import BaseModel


class City(BaseModel):
    """A class representing a city."""

    def __init__(self, *args, **kwargs):
        """Initialize the City instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """Return the string representation of the City instance."""
        return "[City] ({}) {}".format(self.id, self.__dict__)
