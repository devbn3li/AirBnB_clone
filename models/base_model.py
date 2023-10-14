#!/usr/bin/python3
"""This module defines the BaseModel class for managing objects.
"""

import uuid
from datetime import datetime
import models


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
    - save: Updates the 'updated_at' attribute with the current datetime.
    - to_dict: Returns a dictionary representation of the object's attributes
        in a specified format.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Unused variable-length positional arguments.
            **kwargs: Variable-length keyword arguments
                representing object attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, date_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            self.save()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all the object's attributes
        with specific formatting.
        """
        our_obj_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                our_obj_dict[key] = value.isoformat()
            else:
                our_obj_dict[key] = value
        return our_obj_dict
