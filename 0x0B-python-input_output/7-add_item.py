#!/usr/bin/python3
"""
This module adds all command line arguments to a Python list and saves them to a file.
"""

import sys
from typing import List
from json import dump, load
from pathlib import Path


def load_items_from_file(file_path: str) -> List[str]:
    """
    Loads a list of items from a JSON file.
    If the file does not exist, an empty list is returned.
    """
    if not Path(file_path).is_file():
        return []
    with open(file_path) as f:
        return load(f)


def save_items_to_file(items: List[str], file_path: str) -> None:
    """
    Saves a list of items to a JSON file.
    """
    with open(file_path, 'w') as f:
        dump(items, f)


if __name__ == "__main__":
    try:
        items = load_items_from_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_items_to_file(items, "add_item.json")

