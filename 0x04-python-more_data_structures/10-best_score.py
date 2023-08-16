#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest  value."""
    if len(a_dictionary) == 0 or not isinstance(a_dictionary):
        return None

    max_key = list(a_dictionary.keys())[0]
    max_num = a_dictionary[max_key]
    for key, value in a_dictionary.items():
        if value > max_num:
            max_num = value
            max_key = key
    return max_key
