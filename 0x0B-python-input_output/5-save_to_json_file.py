#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename: str) -> None:
    """write the object to the file in JSON representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
