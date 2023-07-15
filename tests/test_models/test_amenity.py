#!/usr/bin/python3
"""Testing for amenity class that inherits from basemodel"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Testing the class amenity"""
    def test_amenity_inherits_from_base_model(self):
        """Testng class amenity is a subclass of basemodel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attributes_default_mode(self):
        """Testing the default mode of the class each attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_init_Amenity(self):
        """Testing if the object is Amenity"""
        object_check = Amenity()
        self.assertIsInstance(object_check, Amenity)

    def test_id(self):
        """Testing that id to be unique"""
        first_id = Amenity()
        second_id = Amenity()
        self.assertNotEqual(first_id, second_id)

    def test_amenity_attributes_assigned(self):
        """Testing the attributes of the class amenity being assigned info"""
        amenity = Amenity()
        amenity.name = "All Available"

        self.assertEqual(amenity.name, "All Available")

    def test_amenity_to_dict(self):
        """Testing amenity to dict mode"""
        amenity = Amenity()
        amenity.name = "All Available"

        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['name'], "All Available")
        self.assertEqual(amenity_dict['__class__'], "Amenity")

    def test_amenity_str(self):
        """Testing the string representing of the class city"""
        amenity = Amenity()
        amenity.name = "All Available"

        string_repr = str(amenity)
        expected_repr = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_amenity_save(self):
        """Testing the save mode in relation to the class amenity"""
        amenity = Amenity()
        old_updated_at = amenity.updated_at
        amenity.save()
        new_updated_at = amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
