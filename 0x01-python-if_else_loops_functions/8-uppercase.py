#!/usr/bin/python3

# Print the ASCII alphabet in reverse order, alternating lowercase and uppercase.
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c - 32 if c % 2 == 0 else c), end="")
print("")
