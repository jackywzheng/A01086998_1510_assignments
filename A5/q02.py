"""Question 2."""

# Jacky Zheng
# Gray Chen

import doctest


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor between two non-zero integers.

    PARAM: a, a non-zero integer
    PARAM: b, a non-zero integer
    PRECONDITION: a must be a non-zero integer
    PRECONDITION: b must be a non-zero integer
    RETURN: the greatest common divisor

    >>> gcd(-25, 15)
    5

    >>> gcd(270, 192)
    6
    """
    if type(a) is not int or type(b) is not int:
        raise ValueError('a and b must be non-zero integers!')
    else:
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a != 0 and b != 0 and abs(a) > abs(b):  # Need absolute value to handle negatives
            return gcd(b, a % b)
        else:
            return gcd(a, b % a)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()

