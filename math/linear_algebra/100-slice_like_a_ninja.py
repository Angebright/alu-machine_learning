#!/usr/bin/env python3
"""Module for slicing a numpy.ndarray along specific axes."""


def np_slice(matrix, axes={}):
    """Slice a matrix along specific axes."""
    slices = [slice(None)] * matrix.ndim
    for axis, sl in axes.items():
        slices[axis] = slice(*sl)
    return matrix[tuple(slices)]
