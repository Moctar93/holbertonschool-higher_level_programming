#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in range(len(row)):
            print("{:d}".format(row[num]), end=" ")
            if num != len(row) - 1:
                print(" ", end=" ")
                print()
