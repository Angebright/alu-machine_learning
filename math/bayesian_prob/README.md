# Bayesian Probability

Python 3 / numpy project on Bayes' rule, using a binomial model of the
probability that patients taking a drug develop severe side effects.

## Files

| File | Description |
|------|-------------|
| `0-likelihood.py` | `likelihood(x, n, P)`: likelihood of the data for each hypothetical probability in `P` |
| `1-intersection.py` | `intersection(x, n, P, Pr)`: likelihood multiplied by the prior for each probability |
| `2-marginal.py` | `marginal(x, n, P, Pr)`: marginal probability of obtaining the data |
| `3-posterior.py` | `posterior(x, n, P, Pr)`: posterior probability of each hypothesis given the data |

## Requirements

- Ubuntu 16.04 LTS, python3 (3.5), numpy (1.15), pycodestyle 2.5
- Only `import numpy as np` is allowed
