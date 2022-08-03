#!/usr/bin/python3
"""
Mylist class
"""


class MyList(list):
    """set sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
