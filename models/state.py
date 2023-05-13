from models.base_model import BaseModel


class State(BaseModel):
    """A class representing a state."""

    def __init__(self, *args, **kwargs):
        """Initialize the State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
