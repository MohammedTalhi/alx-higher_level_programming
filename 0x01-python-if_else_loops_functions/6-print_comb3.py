#!/usr/bin/python3

# Print all possible different combinations of two digits in ascending order.
# The two digits must be different - 01 and 10 are considered identical.
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            # Print the last combination without a trailing comma.
            print("{}{}".format(digit1, digit2))
        else:
            # Print the combination with a trailing comma.
            print("{}{}".format(digit1, digit2), end=", ")
