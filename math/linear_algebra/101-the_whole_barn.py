#!/usr/bin/env python3
"""Module for adding two matrices of any dimension."""


def add_matrices(mat1, mat2):
    """Add two matrices element-wise. Return None if shapes differ."""
    if _matrix_shape(mat1) != _matrix_shape(mat2):
        return None
    return _add_matrices(mat1, mat2)


def _matrix_shape(matrix):
    """Recursively determine the shape of a matrix."""
    if isinstance(matrix, list):
        return [len(matrix)] + _matrix_shape(matrix[0])
    return []


def _add_matrices(mat1, mat2):
    """Recursively add two matrices element-wise."""
    if isinstance(mat1, list):
        return [_add_matrices(a, b) for a, b in zip(mat1, mat2)]
    return mat1 + mat2
