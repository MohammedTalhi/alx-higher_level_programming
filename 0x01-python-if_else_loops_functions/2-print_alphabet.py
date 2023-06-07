#!/usr/bin/python3
# 2-print_alphabet.py

# Print the alphabet in lowercase, not followed by a new line.

# Loop through the ASCII range of lowercase letters (97 to 122)
for ascii_value in range(97, 123):
    # Convert the ASCII value to its corresponding character and print it
    print("{}".format(chr(ascii_value)), end="")
