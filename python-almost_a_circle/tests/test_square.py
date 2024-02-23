#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
import json
import sys
import os
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestSquare(unittest.TestCase):
    """Tests the Square class."""

    def test_initialisation(self):
        """Initialise the square"""
        s1 = Square(1)

        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)

        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)

        self.assertIsInstance(s3, Square)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

        with self.assertRaises(TypeError):
            s4 = Square("1")

        with self.assertRaises(TypeError):
            s5 = Square(1, "2")

        with self.assertRaises(TypeError):
            s6 = Square(1, 2, "3")

        s7 = Square(1, 2, 3, 4)

        self.assertIsInstance(s7, Square)
        self.assertEqual(s7.size, 1)
        self.assertEqual(s7.x, 2)
        self.assertEqual(s7.y, 3)
        self.assertEqual(s7.id, 4)

        with self.assertRaises(ValueError):
            s8 = Square(-1)

        with self.assertRaises(ValueError):
            s9 = Square(1, -2)

        with self.assertRaises(ValueError):
            s10 = Square(1, 2, -3)

        with self.assertRaises(ValueError):
            s11 = Square(0)

    def test__str__(self):
        """Test __str__ method."""
        s1 = Square(1, 2, 3, 4)

        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s1 = Square(1, 2, 3, 4)

        self.assertEqual(s1.to_dictionary(), {
                         'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_update_1(self):
        """Test update method."""
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)

        s1.update()

        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    def test_update_2(self):
        """Test update method."""
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)

        s1.update(89)

        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_3(self):
        """Test update method."""
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)

        s1.update(89, 1)

        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_4(self):
        """Test update method."""
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)

        s1.update(89, 1, 2)

        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_update_5(self):
        """Test update method."""
        Base._Base__nb_objects = 0
        s1 = Square(1, 2, 3, 4)

        s1.update(89, 1, 2, 3)

        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_save_to_file(self):
        """Test save_to_file method."""
        Base._Base__nb_objects = 0
        Square.save_to_file([Square(1)])

        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(), '[{"id": 1, "x": 0, "size": 1, "y": 0}]')

        def test_save_to_file2(self):
            """Test save_to_file([]) in Square."""
            filename = "Square.json"

            Square.save_to_file([])
            self.assertTrue(os.path.exists(filename))

            with open(filename, "r") as f:
                file_content = f.read()

            self.assertEqual(file_content, "[]")

            os.remove(filename)

    def test_load_from_file(self):
        """Test load_from_file method where file does not exist."""
        filename = "nonexistent_file.txt"

        with self.assertRaises(TypeError):
            Square.load_from_file(filename)

    def test_load_from_file_2(self):
        """Test load_from_file method where file exists."""
        Base._Base__nb_objects = 0
        Square.save_to_file([Square(1, 2)])
        list_output = Square.load_from_file()

        expected_output = [Square(1, 2)]
        self.assertNotEqual(str(list_output), str(expected_output))

    def test_size_getter(self):
        """Test size getter method."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_setter(self):
        """Test size setter method."""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_size_setter_invalid_type(self):
        """Test size setter method with invalid type."""
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "invalid"

    def test_size_setter_invalid_value(self):
        """Test size setter method with invalid value."""
        s1 = Square(5)
        with self.assertRaises(ValueError):
            s1.size = -5

    def test_area(self):
        """Test area method."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_display(self):
        """Test display method."""
        s1 = Square(3, 2, 1)
        expected_output = "\n" \
            "  ###\n" \
            "  ###\n" \
            "  ###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s1.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_update(self):
        """Test update method."""
        s1 = Square(5)
        s1.update(10, 7, 2, 3)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s1 = Square(5, 2, 3, 10)
        self.assertEqual(s1.to_dictionary(), {
            'id': 10, 'size': 5, 'x': 2, 'y': 3
        })


if __name__ == "__main__":
    unittest.main()
