#!/usr/bin/python3

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def sub(a, b):
    """Return the difference between two numbers."""
    return a - b

def mul(a, b):
    """Return the product of two numbers."""
    return a * b

def div(a, b):
    """Return the quotient of two numbers."""
    return a / b

if __name__ == "__main__":
    """Print the sum, difference, multiplication, and division of 10 and 5."""
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
