#!/usr/bin/python3
"""Module to get BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User inherit from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
