#!/usr/bin/python3

"""
This module contains a function
that creates an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.
    """
    with open(filename) as file:
        return json.load(file)
