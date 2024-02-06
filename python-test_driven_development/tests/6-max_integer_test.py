#!/usr/bin/python3

"""
Module with unittests for the function `max_integer`.
"""

# Import the `unittest` module.
import unittest

# Import the `max_integer` function from the module '6-max_integer'
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """
    A test class for the 'max_integer' function.

    This class defines a series of test cases to validate the behavior of the 'max_integer' function.
    It includes tests for basic functionality, handling of various input scenarios, and error cases.
    """

    # Test case for the basic functioning of the `max_integer` function.
    def test_basic_functioning(self):
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)
        self.assertEqual(max_integer([2, 6, 4]), 6)
        self.assertEqual(max_integer([-2, -4, -6, -8]), -2)

    # Test case for lists with multiple maximum values.
    def test_multiple_maximum_values(self):
        self.assertIn(max_integer([8, 2, 4, 6, 8, 8]), [8, 8, 8])

    # Test case for an empty list.
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    # Test case for when the function is called without arguments.
    def test_no_arguments(self):
        self.assertEqual(max_integer(), None)

    # Test case for a non-list argument.
    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            max_integer(2468)

    # Test case for a list with non-integer elements.
    def test_list_is_not_int(self):
        with self.assertRaises(TypeError):
            max_integer(["2", 4, "6", 8], 8)
