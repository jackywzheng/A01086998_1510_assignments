"""Convert second to minutes, hours and days."""

# Jacky Zheng
# A01086998
# 01/30/19

import doctest


def time_calculator(seconds):
    """Convert seconds to minutes, hours, and days in a list of integers.

    PARAM: seconds, a positive integer
    PRECONDITION: seconds must be a positive integer
    POSTCONDITION: converts seconds to minutes, hours, and days
    RETURN: an integer list that contains seconds and equivalent minutes, hours, and days
    >>> time_calculator(9999999)
    [115, 17, 46, 39]
    >>> time_calculator(222222)
    [2, 13, 43, 42]
    """
    seconds = int(seconds)
    days = seconds // 86400
    hours = seconds % 86400 // 3600
    minutes = seconds % 86400 % 3600 // 60
    seconds = seconds % 86400 % 3600 % 60
    time_list = [days, hours, minutes, seconds]  # Created a list that stores these variables in order
    return time_list


def main():
    """Drives the function."""
    print(time_calculator())
    doctest.testmod()


if __name__ == '__main__':
    main()

