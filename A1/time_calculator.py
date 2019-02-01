"""Convert second to minutes, hours and days."""

# Jacky Zheng
# A01086998
# 01/30/19

import doctest


def time_calculator(seconds):
    """Convert seconds to minutes, hours, and days in a list of integers.

    >>> time_calculator(86400)
    [1, 24, 1440, 86400]
    >>> time_calculator(200000)
    [2, 55, 3333, 200000]

    PARAM: seconds, a positive integer
    PRECONDITION: seconds must be a positive integer
    POSTCONDITION: converts seconds to minutes, hours, and days
    RETURN: an integer list that contains seconds and equivalent minutes, hours, and days"""
    seconds = int(seconds)
    minutes = seconds // 60
    hours = seconds // 3600
    days = seconds // 86400
    time_list = [days, hours, minutes, seconds]  # Created a list that stores these variables in order
    return time_list


def main():
    print(time_calculator(200000))
    doctest.testmod()


if __name__ == '__main__':
    main()

