#!/usr/bin/python3
# 0-print_list_integer.py
# Douglas Amoo-Sargon <douglasbiomed3@gmail.com>


def print_list_integer(my_list=[]):
    """Print all integers of a list.

    Args:
        my_list: list of integers
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
