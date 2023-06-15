#!/usr/bin/python3

def to_subtract(list_num):
    """
    Calculate the difference between the maximum value in a list and the sum of the other values.

    Args:
        list_num (list): The list of numbers.

    Returns:
        The difference between the maximum value and the sum of the other values in the list.
    """
    to_subtract_value = 0
    max_value = max(list_num)

    for n in list_num:
        if max_value > n:
            to_subtract_value += n

    return max_value - to_subtract_value


def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string.

    Returns:
        int: The converted integer value. Returns 0 if the input is empty or not a string.
    """
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    num += to_subtract(list_num)

    return num
