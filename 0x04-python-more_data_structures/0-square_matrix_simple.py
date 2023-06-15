#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a copy of the matrix to avoid modifying the original
    new_matrix = matrix.copy()

    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Apply the square function to each element in the current row
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return new_matrix
