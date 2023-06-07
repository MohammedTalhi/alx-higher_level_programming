#!/usr/bin/python3

# Function to print the last digit of a number and return it.
def print_last_digit(number):
    """Print the last digit of a number and return it."""
    # Take the absolute value of the number to handle negative numbers.
    absolute_number = abs(number)
    # Calculate the last digit by taking the remainder when divided by 10.
    last_digit = absolute_number % 10
    # Print the last digit without a newline character.
    print(last_digit, end="")
    # Return the last digit.
    return last_digit

