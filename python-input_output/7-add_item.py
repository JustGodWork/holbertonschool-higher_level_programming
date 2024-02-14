#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a Python list,
and then save them to a file.
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
args = sys.argv[1:]
filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
    my_list.extend(args)
except (FileNotFoundError, AttributeError):
    my_list = []

save_to_json_file(my_list, filename)
