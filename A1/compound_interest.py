"""Calculate compound interest."""

# Jacky Zheng
# A01086998
# 01/30/19

import doctest


def compound_interest(p, r, n, t):
    """Calculate compound interest.

    Calculate compound interest given the original principal amount, annual
    interest rate, number of times per year the interest is compounded, and the number of years for growth.
    a = the amount of money in the account after the specified number of years
    p = the principal amount that was originally deposited into the account
    r = the annual interest rate
    n = the number of times per year that the interest is compounded
    t = the specified number of years
    PARAM: p, a positive float
    PARAM: r, a positive float
    PARAM: n, an integer  # Note that 10% is 0.10, not 10.0
    PARAM: t, an integer
    PRECONDITION: p must be a positive float
    PRECONDITION: r must be a positive float
    PRECONDITION: n must be an integer
    PRECONDITION: t must be an integer
    RETURN: a, the amount of money in the account after compound interest
    >>> compound_interest(50000, 0.1, 2, 10)
    132664.88525722112
    """
    a = float(p) * (1 + float(r) / int(n)) ** (int(n) * int(t))
    return float(a)


def main():
    """Drives the function."""
    print(compound_interest(10, 0.01, 1, 1))
    doctest.testmod()


if __name__ == '__main__':
    main()
