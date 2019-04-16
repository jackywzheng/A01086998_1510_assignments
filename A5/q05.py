"""Question 5."""

# Jacky Zheng
# Gray Chen

import doctest


def cashmoney(money: float) -> dict:
    """Count the minimum amount of change needed to represent a double.

    PARAM: money, a positive double float
    PRECONDITION: money must be a positive double float
    RETURN: a minimum amount of change needed to represent a double as a dictionary

    >>> cashmoney(66.63)
    {100: 0, 50: 1, 20: 0, 10: 1, 5: 1, 2: 0, 1: 1, 0.25: 2, 0.1: 1, 0.05: 0, 0.01: 3}

    >>> cashmoney(101.11)
    {100: 1, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 1, 0.25: 0, 0.1: 1, 0.05: 0, 0.01: 1}
    """
    if money < 0:
        raise ValueError("The money you enter cannot be less than zero.")
    change = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    money = int(money * 100)
    while money > 0:
        for keys in change:
            keys *= 100
            if money // keys > 0:
                change[keys / 100] = int(money // keys)
                money -= keys * (money // keys)
            else:
                continue
    return change


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
