#!/usr/bin/python3
"""
This module defines the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city in the project.

    Attributes:
        state_id (str): The ID of the state that the city belongs to.
        name (str): The name of the city.

    Inherits:
        BaseModel: The base model class.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing
                instance attributes.

        The City class inherits from BaseModel and initializes its attributes
            using BaseModel's __init__ method.
        Additional attributes specific to City can be set from kwargs.
        """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.

        The dictionary includes all instance attributes and necessary
            information to recreate the instance.
        """
        obj_dict = super().to_dict()
        obj_dict["state_id"] = self.state_id
        obj_dict["name"] = self.name
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.

        The string representation follows the format: "[<class name>]
            (<id>) <attribute dictionary>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.
                                     __dict__)
