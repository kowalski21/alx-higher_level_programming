#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list with truthy."""
    p_list = []
    for item in my_list:
        if item % 2 == 0:
            p_list.append(True)
        else:
            p_list.append(False)
    return (p_list)
