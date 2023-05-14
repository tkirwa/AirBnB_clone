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

    Inherits from:
        BaseModel (class): Base model class from which Amenity class inherits.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of Amenity.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing
                instance attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.
        """
        amenity_dict = super().to_dict()
        amenity_dict["name"] = self.name
        return amenity_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)
