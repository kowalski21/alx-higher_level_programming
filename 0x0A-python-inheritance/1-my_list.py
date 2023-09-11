#!/usr/bin/python3
# 1-my_list.py


class MyList(list):
    """Subclass list object and add custom function"""

    def print_sorted(self):
        """Print items in sorted order"""
        print(sorted(self))
