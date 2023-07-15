#!/usr/bin/python3
"""Testing for the filestorage"""
import unittest
from models import storage
from models.city import City
from models.review import Review
import os
import json
import models
from models.base_model import BaseModel
from models import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unit Testing implementation for the filestorage file"""
    def setUp(self):
        """This method runs before each test case."""
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.storage = FileStorage()
        storage.__objects = {}

    def tearDown(self):
        """This method runs after each test case, cleaning up resources."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test if all() returns the correct dictionary of objects"""
        obj1 = BaseModel()
        obj2 = City()
        self.storage.new(obj1)
        self.storage.new(obj2)
        objects = self.storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", objects)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", objects)

    def test_new(self):
        """Test for new method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", self.storage.all())

    def test_save_reload(self):
        """Testing for save and reloading of the filestorage file"""
        obj1 = BaseModel()
        obj2 = City()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        storage.__objects = {}
        self.storage.reload()

        objects = storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", objects)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", objects)

    def test_save_no_file(self):
        """Test if save() works correctly when the file does not exist."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.isfile(self.file_path))


if __name__ == "__main__":
    unittest.main()
