#!/usr/bin/python3

# Print the alphabet in lowercase, excluding the letters 'q' and 'e', not followed by a new line.
for ascii_value in range(97, 123):
    current_letter = chr(ascii_value)
    
    # Check if the current letter is not 'q' and not 'e'
    if current_letter != 'q' and current_letter != 'e':
        print("{}".format(current_letter), end="")
