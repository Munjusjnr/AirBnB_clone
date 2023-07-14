#!/usr/bin/python3
"""A class city that inherits from another class basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defining a class city

    Public Class Attributes:
        state_id: State identification
        name: the name of the city
    """
    state_id = ""
    name = ""
