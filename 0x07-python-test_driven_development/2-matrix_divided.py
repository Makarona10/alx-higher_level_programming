#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """
        Divides all matrix elements by a number

        args:
            matrix: 2d list of numbers will be divided
            div: The number that all numbers will be divided by

        Return: A new list of divided numbers
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    x = len(matrix[0])
    z = 0
    new = [[] for _ in range(len(matrix))]
    for row in matrix:
        n = 0
        for element in row:
            if type(element) != float and type(element) != int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new[z].insert(n ,round(element / div, 2))
            n += 1
        y = len(matrix[z])
        if x != y:
            raise TypeError("Each row of the matrix must have the same size")
        z += 1
    return new