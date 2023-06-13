#!/usr/bin/python3

def max_integer(my_list=None):
    if my_list is None or len(my_list) == 0:
        return None
    else:
        maximum = my_list[0]
        for num in my_list:
            if num > maximum:
                maximum = num
        return maximum
