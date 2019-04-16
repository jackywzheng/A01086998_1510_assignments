"""Question 1."""

# Jacky Zheng
# Gray Chen

from math import sqrt
import doctest


def sum_of_primes(upperbound: int) -> int:
    """Calculate the sum of primes from 2 to upperbound.

    PARAM: upperbound, a positive int
    PRECONDITION: upperbound must be a positive int
    RETURN: the sum of primes from 2 to upperbound

    >>> sum_of_primes(5)
    10

    >>> sum_of_primes(11)
    28
    """
    sieve = list(range(2, upperbound + 1))  # Starts at 2 since 0 and 1 are not prime
    if upperbound < 0:
        raise ValueError("upperbound must be a positive integer!")
    for num in range(2, int(sqrt(upperbound)) + 1):
        for i in range(num, int(upperbound)):
            try:
                sieve.remove(num * i)
            except ValueError:
                continue
    return sum(sieve)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
