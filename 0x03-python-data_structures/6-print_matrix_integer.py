#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for letter in row:
            print("{:d}".format(letter), end=" " if letter != row[-1] else "")
        print()
