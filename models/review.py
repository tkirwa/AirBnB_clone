from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing a review."""

    def __init__(self, *args, **kwargs):
        """Initialize the Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
