#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Find the elements that are unique to either set_1 or set_2 (exclusive OR operation)
    different_set = set_1 ^ set_2

    return different_set
