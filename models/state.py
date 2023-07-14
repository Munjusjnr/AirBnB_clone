#!/usr/bin/python3
"""A class state inheriting from another class basemodel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Definning a class state inheriting basemodel

    Public Class Attribute:
        name: referencing the name of the state
    """
    name = ""
