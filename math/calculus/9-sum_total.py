#!/usr/bin/env python3
"""Module for calculating the sum of squares from 1 to n."""


def summation_i_squared(n):
    """Calculate the sum of i^2 for i from 1 to n."""
    if not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
