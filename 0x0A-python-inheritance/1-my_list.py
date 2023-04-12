#!/usr/bin/python3
"""This module inherits from the list class"""

class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))

if __name__ == "__main__":
    lst = MyList([1, 5, 2, 7, 3])
    lst.print_sorted()
