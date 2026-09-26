#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix."""
minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix."""
    m = minor(matrix)
    return [[val * ((-1) ** (i + j)) for j, val in enumerate(row)]
            for i, row in enumerate(m)]
