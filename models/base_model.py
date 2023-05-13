#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class serves as the base class for all...
      other models in the project.
    It defines common attributes and methods..
        that are inherited by other classes.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime.datetime): DateTime object representing the..
         creation timestamp.
        updated_at (datetime.datetime): DateTime object representing...
            the last update timestamp.

    Methods:
        __init__(*args, **kwargs): Initializes a new instance of BaseModel.
        __str__(): Returns a string representation of the instance.
        save(): Updates the updated_at attribute to the current timestamp.
        to_dict(): Converts the instance to a dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments containing...
             instance attributes.

        If kwargs is not empty, it populates the instance attributes from the..
         dictionary representation.
        Otherwise, it generates a new id and sets the creation and update...
         timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.

        The string representation follows the format: "[<class name>] (<id>)...
         <attribute dictionary>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.
                                     __dict__)

    def save(self):
        """
        Updates the updated_at attribute to the current timestamp.

        This method should be called whenever an attribute of the instance is..
         modified.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.

        The dictionary includes all instance attributes and necessary...
         information to recreate the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
