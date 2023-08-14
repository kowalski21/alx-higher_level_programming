#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(my_list, idx, element):
    """New inplace list"""
    orig_list = my_list[::]
    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    orig_list[idx] = element
    return (orig_list)
