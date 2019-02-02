"""Generate 6 random numbers in the range of [0, 49] and sort them lowest to highest."""

# Jacky Zheng
# A01086998
# 01/30/19

import random


def number_generator():
    """Generate and sort 6 random numbers from lowest to highest in the range of [0, 49].
    RETURN: 6 randomly generated numbers in the range of [0, 49] from lowest to highest in a list"""
    lottery_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    lottery = random.sample(lottery_range, 6)  # Takes 6 random numbers from the lottery_range list
    return sorted(lottery)


def main():
    """Drives the function."""
    print(number_generator())


if __name__ == '__main__':
    main()
