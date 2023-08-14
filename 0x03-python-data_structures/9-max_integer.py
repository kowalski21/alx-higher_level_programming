#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    """Find the max integer of a list."""
    if not my_list:
        return None
    maxi = my_list[0]
    for i in my_list:
        if i > maxi:
            maxi = i
    return maxi
