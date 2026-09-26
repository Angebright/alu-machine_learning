#!/usr/bin/env python3
"""Module for concatenating two matrices along a specific axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis."""
    return _cat_matrices(mat1, mat2, axis)


def _matrix_shape(matrix):
    """Recursively determine the shape of a matrix."""
    if isinstance(matrix, list):
        return [len(matrix)] + _matrix_shape(matrix[0])
    return []


def _cat_matrices(mat1, mat2, axis):
    """Recursively concatenate two matrices along a specific axis."""
    if axis == 0:
        if _matrix_shape(mat1)[1:] != _matrix_shape(mat2)[1:]:
            return None
        return mat1 + mat2
    if (not isinstance(mat1, list) or not isinstance(mat2, list)
            or len(mat1) != len(mat2)):
        return None
    result = []
    for sub1, sub2 in zip(mat1, mat2):
        sub_result = _cat_matrices(sub1, sub2, axis - 1)
        if sub_result is None:
            return None
        result.append(sub_result)
    return result
