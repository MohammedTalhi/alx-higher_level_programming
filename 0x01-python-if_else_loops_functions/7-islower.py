#!/usr/bin/python3

# Function to check if a character is lowercase.
def is_lower_case(character):
    """Check if a character is lowercase."""
    if ord(character) >= 97 and ord(character) <= 122:
        return True
    else:
        return False

