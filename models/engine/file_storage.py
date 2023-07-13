#!/usr/bin/python3
"""Class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """A FileStorage class

    Private class Attributes:
        __file_path: string path to json file
        __objects: An empty dictionary that will store all objects name-id
    """

    __file_path = "/AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the json file"""
        emt_dict = {}
        for key, val in FileStorage.__objects.items():
            emt_dict[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            f.write(json.dumps(emt_dict))

    def reload(self):
        """deserializes the JSON file to __objects only if the
        JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as h:
                my_dict = json.loads(h.read())
                for key, val in my_dict.items():
                    inst = eval(val['__class__'])(**val)
                    self.new(inst)
        except FileNotFoundError:
            pass
