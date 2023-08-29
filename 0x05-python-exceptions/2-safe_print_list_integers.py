#!/usr/bin/python3
# 2-safe_print_list_integers.py


def safe_print_list_integers(my_list=[], x=0):
    """Print the list of elements of integers
    with the specified value

    Args:
        my_list (list): The list to print elements from
        x (int): The number of my_list to print
    Returns:
        The x number of elements printed
    """

    counter = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    print("")
    return counter
