#!/usr/bin/python3
"""
    Function file for pascal_triangle().
"""


def pascal_triangle(n):
    """
        Return s alist of lists of integers Pascal's triangle of n.
        Arguments:
            n (int): Size of the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
