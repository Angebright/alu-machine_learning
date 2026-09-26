#!/usr/bin/env python3
"""Module for calculating the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not isinstance(C, (int, float)):
        return None
    integral = [C]
    for i, coef in enumerate(poly):
        new_coef = coef / (i + 1)
        if new_coef == int(new_coef):
            new_coef = int(new_coef)
        integral.append(new_coef)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
