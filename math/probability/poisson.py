#!/usr/bin/env python3
"""Poisson distribution module"""


class Poisson:
    """Represents a Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initialize with data or a given lambtha"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the PMF for k successes"""
        k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        fact = 1
        for i in range(1, k + 1):
            fact *= i
        return (self.lambtha ** k) * (e ** -self.lambtha) / fact

    def cdf(self, k):
        """Calculates the CDF for k successes"""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
