#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b):
    """Print bytecodes."""
    from magic_calculation_102 import add, sub

    if b < a:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c

    else:
        return sub(a, b)
