#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename: str = "", text: str = "") -> int:
    """Appends a string to the end of a UTF8 text file

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        The number of characters appended.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        characters_appended = file.write(text)
    return characters_appended
