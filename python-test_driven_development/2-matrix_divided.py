#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with the result of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If the rows of the matrix are of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if type(matrix) is not list or matrix == []:
        raise TypeError(error_msg)

    new_matrix = []

    for row in matrix:
        if type(row) is not (list) or row == []:
            raise TypeError(error_msg)
        elif len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for number in row:
            if type(number) not in (int, float):
                raise TypeError(error_msg)
            new_row.append(round(number / div, 2))
        new_matrix.append(new_row)

    return new_matrix
