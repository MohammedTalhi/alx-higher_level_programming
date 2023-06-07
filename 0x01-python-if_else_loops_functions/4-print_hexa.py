#!/usr/bin/python3

# Print numbers 0 to 98 in decimal and hexadecimal.
for decimal_number in range(0, 99):
    hexadecimal_number = hex(decimal_number)
    print("{} = {}".format(decimal_number, hexadecimal_number))

