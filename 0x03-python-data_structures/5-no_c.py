#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and C from a string."""
    tmp_list = list(my_string)
    new_string = ""
    for item in tmp_list:
        if item not in ["C", "c"]:
            new_string += item
    return new_string


print(no_c("School boxc"))
