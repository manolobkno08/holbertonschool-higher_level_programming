#!/usr/bin/python3
"""
Function that return div of two lists by element
Doctest check the tests
always success
"""


def matrix_divided(matrix, div):
    """Validate div value"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Check if the matrix is a list of integers and floats"""
    messages_m = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == None:
        raise TypeError(messages_m)
    if type(matrix) is not list:
        raise TypeError(messages_m)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(messages_m)
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(messages_m)

    """Check rows of matrix should be the same size"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """Divide index by div value"""
    new_list = []
    for row in matrix:
        new_list.append(list(map(lambda x: round(x / div, 2), row)))
    return new_list
