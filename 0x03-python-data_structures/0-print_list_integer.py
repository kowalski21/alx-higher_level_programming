#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """A function that prints all integers in a list
    my_list : a list of integers
    """
    for item in my_list:
        print("{:d}".format(item))
