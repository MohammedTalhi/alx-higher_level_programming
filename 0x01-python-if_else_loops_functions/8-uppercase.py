#!/usr/bin/python3

# Function to print a string in uppercase.
def uppercase(string):
    """Print a string in uppercase."""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert lowercase character to uppercase by subtracting 32 from its ASCII value.
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")


