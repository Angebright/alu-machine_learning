#!/usr/bin/env python3
"""Normal distribution module"""


class Normal:
    """Represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize with data or a given mean and stddev"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            n = len(data)
            self.mean = float(sum(data) / n)
            var = sum((x - self.mean) ** 2 for x in data) / n
            self.stddev = float(var ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of x"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the PDF for x"""
        pi = 3.1415926536
        e = 2.7182818285
        z = (x - self.mean) / self.stddev
        return (1 / (self.stddev * (2 * pi) ** 0.5)) * e ** (-0.5 * z ** 2)

    def cdf(self, x):
        """Calculates the CDF for x"""
        pi = 3.1415926536
        z = (x - self.mean) / (self.stddev * 2 ** 0.5)
        erf = z - z ** 3 / 3 + z ** 5 / 10 - z ** 7 / 42 + z ** 9 / 216
        erf *= 2 / pi ** 0.5
        return 0.5 * (1 + erf)
