#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix."""
    c = cofactor(matrix)
    n = len(c)
    return [[c[j][i] for j in range(n)] for i in range(n)]
