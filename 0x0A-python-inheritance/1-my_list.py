#!/usr/bin/python3
"""The module inherits from the class list"""

class MyList(list):
    """The class that inherits from list"""
    class SortedList(list):
    """
    A custom list class that supports printing the sorted list using the
    print_sorted method.
    """
    def print_sorted(self):
        """
        Prints the sorted list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
