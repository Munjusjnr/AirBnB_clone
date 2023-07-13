#!/usr/bin/python3
"""A class amenity inheriting from another class basemodel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defining a class amenity

    Public Attributes:
        name: name of amenites needed
    """
    name = ""
