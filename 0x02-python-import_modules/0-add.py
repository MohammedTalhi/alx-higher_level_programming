#!/usr/bin/python3

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
