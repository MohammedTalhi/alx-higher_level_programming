#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Convert the keys of the dictionary to a list
    ordered_keys = list(a_dictionary.keys())

    # Sort the list of keys in ascending order
    ordered_keys.sort()

    # Iterate over the ordered keys and print each key-value pair
    for key in ordered_keys:
        value = a_dictionary.get(key)
        print("{}: {}".format(key, value))
