#!/usr/bin/python3
"""This module defines the BaseModel class for managing objects.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    The BaseModel class defines common attributes and methods
    for other classes.

    Public instance attributes:
    - id (str): A unique identifier generated using uuid4.
    - created_at (datetime): A timestamp representing
        when the instance is created.
    - updated_at (datetime): A timestamp representing
        the last update time of the instance.

    Public instance methods:
    - __str__: Returns a string representation of the object.
    - save: Updates the `updated_at` attribute with the current datetime.
    - to_dict: Returns a dictionary representation of the object's attributes
        in a specified format.
    """
    def __init__(self):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all the object's attributes
        with specific formatting.
        """
        our_obj_dict = self.__dict__.copy()
        our_obj_dict["__class__"] = self.__class__.__name__
        our_obj_dict["created_at"] = self.created_at.isoformat()
        our_obj_dict["updated_at"] = self.updated_at.isoformat()

        return our_obj_dict
