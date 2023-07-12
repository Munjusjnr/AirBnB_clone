#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():

    __file_path = "/AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        emt_dict = {}
        for key, val in FileStorage.__objects.items():
            emt_dict[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            f.write(json.dumps(emt_dict))

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as h:
                my_dict = json.loads(h.read())
                for key, val in my_dict.items():
                    inst = eval(val['__class__'])(**val)
                    self.new(inst)
        except FileNotFoundError:
            pass
