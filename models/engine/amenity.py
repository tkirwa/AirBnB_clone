#!/usr/bin/python3
"""
This module defines the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity.

    Attributes:
        name (str): The name of the Amenity.

    Inherits:
        BaseModel: The base class for all models in the project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing instance attributes.

        Attributes:
            name (str): The name of the Amenity.

        Inherits:
            BaseModel.__init__(): The initialization method of the BaseModel.
        """
        self.name = ""
        super().__init__(*args, **kwargs)
