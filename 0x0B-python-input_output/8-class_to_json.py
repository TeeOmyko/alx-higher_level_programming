#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_dict(obj):
    """Returns a dictionary of the object's instance variables."""
    return obj.__dict__
