#!/usr/bin/python3

def number_keys(a_dictionary):
    # Initialize a variable to store the number of keys in the dictionary
    num_keys = 0

    # Convert the keys of the dictionary to a list
    key_list = list(a_dictionary.keys())

    # Iterate over each key in the list and increment the count
    for key in key_list:
        num_keys += 1

    return num_keys
