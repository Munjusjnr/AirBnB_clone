#!/usr/bin/python3
"""Testing the place model inheriting from the basemodel"""
import unittest
import models
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Class Place test implementation"""
    def test_place_inherits_from_base_model(self):
        """Testing place is a subclass of another class"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_default_attributes(self):
        """Testing place default attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_assigments(self):
        """Testing place attributes being assigned information"""
        place = Place()
        place.city_id = "Gt676"
        place.user_id = "879-98"
        place.name = "Gotham"
        place.description = "serene"
        place.number_rooms = 4
        place.number_bathrooms = 4
        place.max_guest = 8
        place.price_by_night = 100
        place.latitude = 8.9
        place.longitude = 10.7
        place.amenity_ids = ["89-789"]

        self.assertEqual(place.city_id, "Gt676")
        self.assertEqual(place.user_id, "879-98")
        self.assertEqual(place.name, "Gotham")
        self.assertEqual(place.description, "serene")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 4)
        self.assertEqual(place.max_guest, 8)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 8.9)
        self.assertEqual(place.longitude, 10.7)
        self.assertEqual(place.amenity_ids, ["89-789"])

    def test_init_Place(self):
        """Testing if the object is Place"""
        object_check = Place()
        self.assertIsInstance(object_check, Place)

    def test_id(self):
        """Testing that id to be unique"""
        first_id = Place()
        second_id = Place()
        self.assertNotEqual(first_id, second_id)

    def test_place_to_dict(self):
        """Testing place attributes in a dictionary"""
        place = Place()
        place.city_id = "Gt676"
        place.user_id = "879-98"
        place.name = "Gotham"
        place.description = "serene"
        place.number_rooms = 4
        place.number_bathrooms = 4
        place.max_guest = 8
        place.price_by_night = 100
        place.latitude = 8.9
        place.longitude = 10.7
        place.amenity_ids = ["89-789"]

        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['city_id'], "Gt676")
        self.assertEqual(place_dict['user_id'], "879-98")
        self.assertEqual(place_dict['name'], "Gotham")
        self.assertEqual(place_dict['description'], "serene")
        self.assertEqual(place_dict['number_rooms'], 4)
        self.assertEqual(place_dict['number_bathrooms'], 4)
        self.assertEqual(place_dict['max_guest'], 8)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 8.9)
        self.assertEqual(place_dict['longitude'], 10.7)
        self.assertEqual(place_dict['amenity_ids'], ["89-789"])
        self.assertEqual(place_dict['__class__'], "Place")

    def test_place_str(self):
        """Testing string representation of the place class"""
        place = Place()
        place.city_id = "Gt676"
        place.user_id = "879-98"
        place.name = "Gotham"
        place.description = "serene"
        place.number_rooms = 4
        place.number_bathrooms = 4
        place.max_guest = 8
        place.price_by_night = 100
        place.latitude = 8.9
        place.longitude = 10.7
        place.amenity_ids = ["89-789"]

        string_repr = str(place)
        expected_repr = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_place_save(self):
        """Testing for updates when saved"""
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        new_updated_at = place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
