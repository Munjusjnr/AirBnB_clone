#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    def test_do_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()

            self.assertIn("Documented commands (type help <topic>):", output)

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue()

            self.assertEqual(output, "")

    def test_do_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")

            self.assertEqual(f.getvalue(), "")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")

            self.assertEqual(f.getvalue(), "")

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Mymodel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Mymodel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 23456712")
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Review.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('State.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('City.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Amenity.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Place.show("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Mymodel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 23456712")
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Review.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('State.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('City.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Amenity.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Place.destroy("id")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Mymodel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            output = f.getvalue().strip()

            self.assertIsInstance(output, str)

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Mymodel")
            output = f.getvalue().strip()

            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 23456712")
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Review.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('State.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('City.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Amenity.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Place.update("id", "attribute_name", "string_value")')
            output = f.getvalue().strip()

            self.assertEqual(output, "** no instance found **")

    def test_do_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()

            self.assertTrue(output.isdigit())
