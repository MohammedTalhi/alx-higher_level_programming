#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Multiply the values of a dictionary by 2.

    Args:
        a_dictionary (dict): The original dictionary.

    Returns:
        dict: A new dictionary with the values multiplied by 2.
    """
    # Create a copy of the dictionary to avoid modifying the original
    new_dict = a_dictionary.copy()

    # Get a list of keys from the copied dictionary
    key_list = list(new_dict.keys())

    # Iterate over each key and multiply its corresponding value by 2
    for key in key_list:
        new_dict[key] *= 2

    return new_dict
