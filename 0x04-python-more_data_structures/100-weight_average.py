#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.

    Args:
        my_list (list): The list of tuples where each tuple contains two values.

    Returns:
        float: The weighted average of the values in the list. Returns 0 if the input list is empty.
    """
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for tup in my_list:
        numerator += tup[0] * tup[1]
        denominator += tup[1]

    return numerator / denominator
