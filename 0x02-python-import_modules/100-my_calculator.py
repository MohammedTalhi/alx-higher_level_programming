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
    """Handle basic arithmetic operations."""
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
