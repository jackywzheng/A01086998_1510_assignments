"""Question 9."""

# Jacky Zheng
# Gray Chen

import doctest


def convert_to_base_ten(number: int, original_base: int) -> int:
    """Return number in base less than 10 to a decimal number.

    PARAM: number, a positive integer
    PARAM: original_base, a positive integer less than 10
    PRECONDITION: number must be a positive integer
    PRECONDITION: original_base must be a positive integer less than 10
    RETURN: the corresponding decimal number

    >>> convert_to_base_ten(101010, 2)
    42
    """
    for digit in str(number):
        if int(digit) >= original_base:
            raise ValueError('You cannot enter a number that is greater than the base!')
    if number < original_base:
        return number
    else:
        return int(str(number)[0]) * (original_base ** (len(str(number)) - 1)) + \
               convert_to_base_ten(int(str(number)[1:]), original_base)


def convert_to_other_base(number: int, base: int) -> str:
    """Convert a decimal number to another base less than 10.

    PARAM: number, a positive integer
    PARAM: base, a positive integer less than 10
    PRECONDITION: number must be a positive integer
    PRECONDITION: base must be a positive integer less than 10
    RETURN: number in corresponding base as a string

    >>> convert_to_other_base(10, 2)
    '1010'
    """
    if number < base:
        return str(number % base)
    else:
        return convert_to_other_base(number//base, base) + str(number % base)


def base_conversion(original_base: int, number: int, destination_base: int) -> int:
    """Convert any number from any base less than 10 to another base less than 10.

    PARAM: original_base, a positive int less than 10
    PARAM: number, a positive integer
    PARAM: destination base, a positive int less than 10
    PRECONDITION: original_base must be a positive int less than 10
    PRECONDITION: number must be a positive int less than 10
    PRECONDITION: destination base must be a positive int less than 10
    RETURN: number in destination base

    >>> base_conversion(10, 1, 2)
    1

    >>> base_conversion(8, 17, 4)
    33
    """
    decimal = convert_to_base_ten(number, original_base)
    return int(convert_to_other_base(decimal, destination_base))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
