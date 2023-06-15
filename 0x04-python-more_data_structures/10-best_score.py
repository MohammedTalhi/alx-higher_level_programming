#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Find the key with the highest value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to search.

    Returns:
        The key with the highest value. If the dictionary is empty, returns None.
    """
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Find the key with the highest value using the max() function
    max_key = max(a_dictionary, key=a_dictionary.get)

    return max_key
