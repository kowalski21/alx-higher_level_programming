#!/usr/bin/python3
# 0-safe_print_list.py


def safe_print_list(my_list=[], x=0):
    """Print x elements in list with exception handle

    Args:
        my_list (list): list to print
        x (int) : number of elements to print

    Returns:
        The number of elements printed
    """
    counter = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            index += 1
        except IndexError:
            break
    print("")
    return counter
