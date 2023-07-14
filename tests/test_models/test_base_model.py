#!/usr/bin/python3
"""Tests for the basemodel class for expected behaviour"""
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the basemodel class
    """
    def test_init_with_no_argument(self):
        """Testing initialization with no arguments"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)


    def test_init_with_arguments(self):
        """Testing initialization with arguments"""
        model_data = {'id': 'test-id', 'created_at': '2022-01-01T00:00:00',
                      'updated_at': '2022-01-02T00:00:00',
                      'name': 'Test Model'}
        model = BaseModel(**model_data)
        self.assertEqual(model.id, 'test-id')
        self.assertEqual(model.created_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))
        self.assertEqual(model.updated_at,
                         datetime.fromisoformat('2022-01-02T00:00:00'))
        self.assertEqual(model.name, 'Test Model')

    def test_init_BaseModel(self):
        """Testing if the object is basemodel"""
        object_check = BaseModel()
        self.assertIsInstance(object_check, BaseModel)

    def test_id(self):
        """Testing that id to be unique"""
        first_id = BaseModel()
        second_id = BaseModel()
        self.assertNotEqual(first_id, second_id)


    def test_str(self):
        """Testing string representation"""
        model = BaseModel()
        string_repr = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(string_repr, expected_str)

    def test_save(self):
        """Testing saving the class basemodel"""
        model = BaseModel()
        update_at_before = model.updated_at
        model.save()
        update_at_after = model.updated_at
        self.assertNotEqual(update_at_after, update_at_before)

    def test_dict(self):
        """Testing class basemodel being converted to dictionary"""
        model_data = {'id': 'test-id', 'created_at': '2022-01-01T00:00:00',
                      'updated_at': '2022-01-02T00:00:00',
                      'name': 'Test Model'}
        model = BaseModel(**model_data)
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], 'test-id')
        self.assertEqual(model_dict['created_at'], '2022-01-01T00:00:00')
        self.assertEqual(model_dict['updated_at'], '2022-01-02T00:00:00')
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
