#!/usr/bin/python3
"""This module imports two foreign functions and contains a class that uses
   them.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """This class is the foundation of a great program.
    """

    def __init__(self, *args, **kwargs):
        """This method initantializes three public instance attributes.

        Args:
            *arg(tuple): This is a tuple that contains parameters
            **kwargs(dict): This is a dictionary that contains parameterd and
            their values.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs != {}:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(val)
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """This is the __str__ method.

        Return:
            str: Information on the class.
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates the time of ``updated_at`` when it is called.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method creates a dictionary of the this class and it's
           instance attributes.

        Return:
            dict: A dictionary containing the instance attributes of this
            class.
        """
        my_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()

            my_dict.update({key: value})

        my_dict.update({"__class__": f"{__class__.__name__}"})
        return my_dict
