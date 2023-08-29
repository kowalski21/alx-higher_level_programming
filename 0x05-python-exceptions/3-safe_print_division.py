#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """Returns division only when there are no errors"""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
