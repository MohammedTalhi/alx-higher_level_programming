#!/usr/bin/python3

# Print numbers 0 to 99 with leading zeros, separated by commas.
for number in range(0, 100):
    if number == 99:
        # Print the last number without a trailing comma.
        print("{}".format(number))
    else:
        # Print the number with leading zeros and a trailing comma.
        print("{:02}".format(number), end=", ")

