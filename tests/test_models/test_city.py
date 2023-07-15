#!/usr/bin/python3
"""Testing for city class that inherits from basemodel"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Testing the class city"""
    def test_city_inherits_from_base_model(self):
        """Testng class city is a subclass of basemodel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes_default_mode(self):
        """Testing the default mode of the class each attribute"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes_assigned(self):
        """Testing the attributes of the class city being assigned info"""
        city = City()
        city.state_id = "GTHstate-id"
        city.name = "Gotham City"

        self.assertEqual(city.state_id, "GTHstate-id")
        self.assertEqual(city.name, "Gotham City")

    def test_init_City(self):
        """Testing if the object is City"""
        object_check = City()
        self.assertIsInstance(object_check, City)

    def test_id(self):
        """Testing that id to be unique"""
        first_id = City()
        second_id = City()
        self.assertNotEqual(first_id, second_id)

    def test_city_to_dict(self):
        """Testing city to dict mode"""
        city = City()
        city.state_id = "GTHstate-id"
        city.name = "Gotham City"

        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['state_id'], "GTHstate-id")
        self.assertEqual(city_dict['name'], "Gotham City")
        self.assertEqual(city_dict['__class__'], "City")

    def test_city_str(self):
        """Testing the string representing of the class city"""
        city = City()
        city.state_id = "GTHstate-id"
        city.name = "Gotham City"

        string_repr = str(city)
        expected_repr = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_city_save(self):
        """Testing for updates when saved"""
        city = City()
        old_updated_at = city.updated_at
        city.save()
        new_updated_at = city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
