#!/usr/bin/python3
"""
This module defines the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review in the project.

    Attributes:
        place_id (str): The ID of the place that the review belongs to.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.

    Inherits:
        BaseModel: The base model class.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Review class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing
                instance attributes.

        The Review class inherits from BaseModel and initializes its attributes
            using BaseModel's __init__ method.
        Additional attributes specific to Review can be set from kwargs.
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.

        The dictionary includes all instance attributes and necessary...
         information to recreate the instance.
        """
        obj_dict = super().to_dict()
        obj_dict["place_id"] = self.place_id
        obj_dict["user_id"] = self.user_id
        obj_dict["text"] = self.text
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.

        The string representation follows the format: "[<class name>] (<id>)
            <attribute dictionary>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.
                                     __dict__)
