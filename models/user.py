#!/usr/bin/python3
"""A class user inheriting from another class basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defining a class user that inherits from another class Basemodel

    Public Class Attributes:
        Email: placeholder for email of the user
        Password: placeholer for user's password
        first_name: first name of the user
        last_name: last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
