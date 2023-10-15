#!/usr/bin/python3
""" Module to get BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
