#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[elem**2 for elem in inner] for inner in matrix]

    return new_matrix
