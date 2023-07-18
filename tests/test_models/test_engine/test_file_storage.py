#!/usr/bin/python3
"""Testing for the filestorage"""
import unittest
from models import storage
from models.city import City
from models.review import Review
import pep8
import os
import json
import models
from models.base_model import BaseModel
from models import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unit Testing implementation for the filestorage file"""
    def setUp(self):
        """This method runs before each test case."""
        self.file_path = "file.json"
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

    def test_pep8(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        path = "tests/test_models/test_engine/test_file_storage.py"
        res = pep8style.check_files(["models/engine/file_storage.py", path])
        self.assertEqual(res.total_errors, 0, "PEP8 style errors found")

    def test_instance_of_file_storage(self):
        """Test if the instance is of the FileStorage class"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_attribute_types(self):
        """Test if the attributes have the correct types"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_updated_at_updates_after_save(self):
        """Test if updated_at attribute updates after calling instance"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_instances_stored_correctly(self):
        """Test if instances of all classes are stored correctly in the file"""
        obj1 = BaseModel()
        obj2 = City()
        obj3 = Review()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()

        with open(self.file_path, 'r') as file:
            data = json.load(file)

        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", data)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", data)
        self.assertIn(f"{obj3.__class__.__name__}.{obj3.id}", data)

    def test_file_path(self):
        """Test if the __file_path attribute has the correct value"""
        path = "file.json"
        self.assertEqual(self.storage._FileStorage__file_path, path)

    def test_base_model_save(self):
        """Test if BaseModel's save method updates the updated_at attribute"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        after_update = obj.updated_at
        self.assertNotEqual(initial_updated_at, after_update)

    def test_file_path_override(self):
        """Test if the __file_path attribute is set to None in the subclass"""
        file_storage_instance = FileStorage()
        self.assertIsNotNone(file_storage_instance._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
