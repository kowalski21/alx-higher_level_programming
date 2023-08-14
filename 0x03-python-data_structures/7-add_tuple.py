#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples together."""
    prep_a = tuple_a + (0, 0)
    prep_b = tuple_b + (0, 0)
    x = prep_b[1] + prep_a[1]
    y = prep_a[0] + prep_b[0]
    return (y, x)
