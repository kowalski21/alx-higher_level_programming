#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """Learn to safely execute functions

    Args:
        fct: function to exec
        args: arguments to functions
    Returns:
        None when error occurs else value
    """
    try:
        func_result = fct(*args)
        return func_result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
