#!/usr/bin/python3
"""Testing the user model inheriting from the basemodel"""
import unittest
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Class User test implementation"""
    def test_user_inherits_from_base_model(self):
        """Testing user is a subclass of another class"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_default_attributes(self):
        """Testing user default attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute_assigments(self):
        """Testing user attributes being assigned information"""
        user = User()
        user.email = "test@mail.com"
        user.password = "lastwords"
        user.first_name = "lee"
        user.last_name = "kramps"

        self.assertEqual(user.email, "test@mail.com")
        self.assertEqual(user.password, "lastwords")
        self.assertEqual(user.first_name, "lee")
        self.assertEqual(user.last_name, "kramps")

    def test_user_to_dict(self):
        """Testing user attributes in a dictionary"""
        user = User()
        user.email = "test@mail.com"
        user.password = "lastwords"
        user.first_name = "lee"
        user.last_name = "kramps"

        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['email'], "test@mail.com")
        self.assertEqual(user_dict['password'], "lastwords")
        self.assertEqual(user_dict['first_name'], "lee")
        self.assertEqual(user_dict['last_name'], "kramps")
        self.assertEqual(user_dict['__class__'], "User")

    def test_user_str(self):
        """Testing string representation of the user class"""
        user = User()
        user.email = "test@mail.com"
        user.password = "lastwords"
        user.first_name = "lee"
        user.last_name = "kramps"

        string_repr = str(user)
        expected_repr = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_user_save(self):
        """Testing for updates when saved"""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
