#!/usr/bin/python3
"""A class place inheriting from another class BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defining a class place

    Public Class Attributes:
        city_id: city identification
        user_id: user identification
        name: name of the place
        description: description of the  place
        number_rooms: number of rooms available
        number_bathrooms: number of rooms available
        max_guest: maximum number of guests to be allowed
        price_by_night: price of the place per night
        latitude: coordinate of the place
        longitude: coordinate of the place
        amenity_ids: amenites identified at the place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
