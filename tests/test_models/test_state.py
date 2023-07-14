#!/usr/bin/python3
"""Testing for amenity class that inherits from basemodel"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Testing the class amenity"""
    def test_state_inherits_from_base_model(self):
        """Testng class state as a subclass of basemodel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes_default_mode(self):
        """Testing the default mode of the class each attribute"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attributes_assigned(self):
        """Testing the attributes of the class state being assigned info"""
        state = State()
        state.name = "Hawaii"

        self.assertEqual(state.name, "Hawaii")

    def test_state_to_dict(self):
        """Testing amenity to dict mode"""
        state = State()
        state.name = "Hawaii"

        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "Hawaii")
        self.assertEqual(state_dict['__class__'], "State")

    def test_state_str(self):
        """Testing the string representing of the class state"""
        state = State()
        state.name = "Hawaii"

        string_repr = str(state)
        expected_repr = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_state_save(self):
        """Testing the save mode in relation to the class state"""
        state = State()
        old_updated_at = state.updated_at
        state.save()
        new_updated_at = state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
