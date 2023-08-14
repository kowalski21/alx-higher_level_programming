#!/usr/bin/python3
# 0-print_list_integer.py
# Douglas Amoo-Sargon <douglasbiomed3@gmail.com>


def print_list_integer(my_list=[]):
    """A function that prints all integers in a list
    my_list : a list of integers
    """
    for item in my_list:
        print("{:d}".format(item))
