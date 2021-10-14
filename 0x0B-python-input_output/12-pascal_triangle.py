#!/usr/bin/python3
"""
Return a Pascal's Triangle
"""


def pascal_triangle(n):
    """Return a triangle"""
    if n <= 0:
        return []

    lim = n - 1

    triangle = [[1]]

    for i in range(lim):
        row = [1]

        if len(triangle[i]) > 1:
            large_prev = len(triangle[i]) - 1

            for j in range(large_prev):
                row.append(triangle[i][j] + triangle[i][j+1])
        row.append(1)
        triangle.append(row)
    return triangle
