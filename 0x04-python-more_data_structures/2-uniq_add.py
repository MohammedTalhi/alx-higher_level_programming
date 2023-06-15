#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store unique elements from the list
    unique_set = set(my_list)

    # Initialize a variable to store the sum of unique elements
    total_sum = 0

    # Iterate over each unique element in the set
    for i in unique_set:
        # Add the current element to the total sum
        total_sum += i

    return total_sum
