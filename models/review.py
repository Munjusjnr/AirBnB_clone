#!/usr/bin/python3
"""A class review inheriting from another class basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defining a class review

    Public class attributes:
        place_id: place identification under review
        user_id: user id of the reviewer
        text: user's written thoughts observed
    """
    place_id = ""
    user_id = ""
    text = ""
