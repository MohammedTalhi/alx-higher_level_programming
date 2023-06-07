#!/usr/bin/python3

# Function to print numbers from 1 to 100 based on certain conditions.
def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            # Multiple of both 3 and 5, print FizzBuzz.
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            # Multiple of 3, print Fizz.
            print("Fizz ", end="")
        elif number % 5 == 0:
            # Multiple of 5, print Buzz.
            print("Buzz ", end="")
        else:
            # Not a multiple of 3 or 5, print the number itself.
            print("{} ".format(number), end="")

