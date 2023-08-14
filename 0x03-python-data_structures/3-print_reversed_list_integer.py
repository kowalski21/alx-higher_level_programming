#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    valid_list = isinstance(my_list, list)
    if valid_list:
        rev_list = my_list[::-1]
        for item in rev_list:
            print("{:d}".format(item))
