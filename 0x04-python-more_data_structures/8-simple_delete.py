#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete a key/value pair from a dictionary.

    Args:
        a_dictionary (dict): The original dictionary.
        key: The key to be deleted.

    Returns:
        dict: The updated dictionary after deleting the key/value pair.
    """
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key/value pair from the dictionary
        del a_dictionary[key]

    return a_dictionary
