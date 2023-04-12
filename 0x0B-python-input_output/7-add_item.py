#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from typing import List
from pathlib import Path

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list_and_save(items: List[str], filename: str) -> None:
    """Adds items to a list and saves it to a JSON file."""
    try:
        items_list = load_from_json_file(filename)
    except FileNotFoundError:
        items_list = []
    items_list.extend(items)
    save_to_json_file(items_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_items_to_list_and_save(args, "add_item.json")

