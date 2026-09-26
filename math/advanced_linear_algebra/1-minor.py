#!/usr/bin/env python3
"""Module for calculating the minor matrix of a matrix."""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Calculate the minor matrix of a matrix."""
    if (not isinstance(matrix, list) or len(matrix) == 0
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if n == 1:
        return [[1]]
    result = []
    for i in range(n):
        row_result = []
        for j in range(n):
            sub = [r[:j] + r[j + 1:] for k, r in enumerate(matrix) if k != i]
            row_result.append(determinant(sub))
        result.append(row_result)
    return result
