#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename: str = "") -> None:
    """Read a text file and output its contents to stdout"""

    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
    print(content, end='')
