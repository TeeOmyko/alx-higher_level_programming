#!/usr/bin/python3
"""Create a UTF-8 text file and write a string to it"""


def write_file(filename: str = "", text: str = "") -> int:
    """Create a text file and write a string to it.

    Args:
        filename (str): The name of the file to create.
        text (str): The text to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written

