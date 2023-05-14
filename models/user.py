#!/usr/bin/python3
"""
This module defines the User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the project.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Inherits:
        BaseModel: The base model class.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the User class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing instance
                attributes.

        The User class inherits from BaseModel and initializes its attributes..
         using BaseModel's __init__ method.
        Additional attributes specific to User can be set from kwargs.
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
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
        obj_dict["email"] = self.email
        obj_dict["password"] = self.password
        obj_dict["first_name"] = self.first_name
        obj_dict["last_name"] = self.last_name
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
