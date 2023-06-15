#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add key/value pairs in a dictionary.

    Args:
        a_dictionary (dict): The original dictionary.
        key: The key to be replaced or added.
        value: The value to be associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    # Replace or add the key/value pair in the dictionary
    a_dictionary[key] = value

    return a_dictionary
