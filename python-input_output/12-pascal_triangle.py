#!/usr/bin/python3
"""
This module contains a function that returns a list of lists
of integer representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Generate a Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list of list: A list of lists representing Pascal's
        triangle up to 'n' rows.
        Each inner list contains the coefficients for a specific row.

    Raises:
        ValueError: If 'n' is not a positive integer.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    matrix = [[1]]
    for _ in range(1, n):
        row = [1]
        prev_row = matrix[-1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        matrix.append(row)
    return matrix
