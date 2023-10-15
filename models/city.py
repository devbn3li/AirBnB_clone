#!/usr/bin/python3
""" Module to get BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City inherit from BaseModel"""

    name = ""
    state_id = ""
