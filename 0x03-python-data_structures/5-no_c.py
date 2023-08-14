#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_string = [item for item in my_string if item != "C" and item != "c"]
    return new_string
