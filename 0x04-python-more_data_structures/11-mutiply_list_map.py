#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in a list by a given number using map() function.

    Args:
        my_list (list): The original list.
        number: The number to multiply each element by.

    Returns:
        list: A new list with each element multiplied by the given number.
    """
    # Use map() function with a lambda function to multiply each element by the number
    multiplied_list = list(map(lambda i: i * number, my_list))

    return multiplied_list
