#!/usr/bin/python3
"""
This module defines the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state in the project.

    Attributes:
        name (str): The name of the state.

    Inherits:
        BaseModel: The base model class.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the State class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing instance attributes.

        The State class inherits from BaseModel and initializes its attributes using BaseModel's __init__ method.
        Additional attributes specific to State can be set from kwargs.
        """
        self.name = ""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.

        The dictionary includes all instance attributes and necessary information to recreate the instance.
        """
        obj_dict = super().to_dict()
        obj_dict["name"] = self.name
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.

        The string representation follows the format: "[<class name>] (<id>) <attribute dictionary>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
