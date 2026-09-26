#!/usr/bin/env python3
"""Module for transposing a 2D matrix."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    return [list(row) for row in zip(*matrix)]
