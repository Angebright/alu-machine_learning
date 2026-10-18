# Multivariate Probability

Python 3 / numpy project on multivariate statistics and the multivariate
normal distribution.

## Files

| File | Description |
|------|-------------|
| `0-mean_cov.py` | `mean_cov(X)`: mean and covariance matrix of a data set of shape `(n, d)` |
| `1-correlation.py` | `correlation(C)`: correlation matrix from a covariance matrix |
| `multinormal.py` | `MultiNormal` class: `mean` and `cov` from data of shape `(d, n)`, and `pdf(x)` at a point of shape `(d, 1)` |

## Requirements

- Ubuntu 16.04 LTS, python3 (3.5), numpy (1.15), pycodestyle 2.5
- Only `import numpy as np` is allowed, and `numpy.cov` is not used
