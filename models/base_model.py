#!/usr/bin/python3
"""
Module containing immutable UUID objects
Defining a class BaseModel that all other inherit from
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """"Initializes public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self,):
        """Returns class name, id and dictionary attribute
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """Update instance attribute with current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
