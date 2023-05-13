#!/usr/bin/python3
"""
This module defines the Place class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place in the project.

    Attributes:
        city_id (str): The ID of the city that the place belongs to.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of amenity IDs associated with the place.

    Inherits:
        BaseModel: The base model class.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Place class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing instance attributes.

        The Place class inherits from BaseModel and initializes its attributes using BaseModel's __init__ method.
        Additional attributes specific to Place can be set from kwargs.
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.

        The dictionary includes all instance attributes and necessary information to recreate the instance.
        """
        obj_dict = super().to_dict()
        obj_dict["city_id"] = self.city_id
        obj_dict["user_id"] = self.user_id
        obj_dict["name"] = self.name
        obj_dict["description"] = self.description
        obj_dict["number_rooms"] = self.number_rooms
        obj_dict["number_bathrooms"] = self.number_bathrooms
        obj_dict["max_guest"] = self.max_guest
        obj_dict["price_by_night"] = self.price_by_night
        obj_dict["latitude"] = self.latitude
        obj_dict["longitude"] = self.longitude
        obj_dict["amenity_ids"] = self.amenity_ids
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.

        The string representation follows the format: "[<class name>] (<id>) <attribute dictionary>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
