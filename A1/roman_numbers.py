"""Convert integer to Roman numeral."""

# Jacky Zheng
# A01086998
# 01/30/19

import doctest


def convert_to_roman_numeral(positive_int):
    """Convert integer to Roman numeral.

    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(9999)
    'MMMMMMMMMCMXCIX'

    PARAM: positive_int, an integer in the range of [1, 10000]
    PRECONDITION: positive_int must be an integer in the range of [1, 10000]
    POSTCONDITION: converts the integer to the equivalent Roman numeral
    RETURN: converted integer as Roman numeral"""
    # Have to use if and elif statements to avoid index out of range error
    if len(str(positive_int)) == 5:
        return thousands_conversion(positive_int)
    elif len(str(positive_int)) == 4:
        return thousands_conversion(positive_int) + hundreds_conversion(positive_int) \
               + tens_conversion(positive_int) + ones_conversion(positive_int)
    elif len(str(positive_int)) == 3:
        return hundreds_conversion(positive_int) + tens_conversion(positive_int) + ones_conversion(positive_int)
    elif len(str(positive_int)) == 2:
        return tens_conversion(positive_int) + ones_conversion(positive_int)
    elif len(str(positive_int)) == 1:
        return ones_conversion(positive_int)
    elif positive_int == 0:
        return '0'


def ones_conversion(positive_int):
    """Convert the ones place of an integer to Roman numeral.

    >>> ones_conversion(4)
    'IV'
    >>> ones_conversion(9)
    'IX'

    PARAM: positive_int[-1], an integer in the range of [0, 9]
    PRECONDITION: positive_int[-1] must be an integer in the range of [0, 9]
    POSTCONDITION: converts the ones place integer to the Roman numeral
    RETURN: converted ones place of an integer as Roman numeral"""
    # I use an index of [-1] to select the one's place as it's on the rightmost place numerically
    positive_int = str(positive_int)
    if int(positive_int[-1]) < 4:
        return 'I' * int(positive_int[-1])  # Can multiply I by the corresponding value as long as it's under 4
    if int(positive_int[-1]) == 4:
        return 'IV'
    if int(positive_int[-1]) == 5:
        return 'V'
    if int(positive_int[-1]) == 6:
        return 'VI'
    if int(positive_int[-1]) == 7:
        return 'VII'
    if int(positive_int[-1]) == 8:
        return 'VIII'
    if int(positive_int[-1]) == 9:
        return 'IX'


def tens_conversion(positive_int):
    """Convert the tens place of an integer to Roman numeral.

    >>> tens_conversion(40)
    'XL'
    >>> tens_conversion(90)
    'XC'

    PARAM: positive_int[-2], an integer in the range of [0, 9]
    PRECONDITION: positive_int[-2] must be an integer in the range of [0, 9]
    POSTCONDITION: converts the tens place integer to the Roman numeral
    RETURN: converted tens place of an integer as Roman numeral"""
    # I use an index of [-2] to select the ten's place, and so forth until the thousands
    positive_int = str(positive_int)
    if int(positive_int[-2]) < 4:
        return 'X' * int(positive_int[-2])
    if int(positive_int[-2]) == 4:
        return 'XL'
    if int(positive_int[-2]) == 5:
        return 'L'
    if int(positive_int[-2]) == 6:
        return 'LX'
    if int(positive_int[-2]) == 7:
        return 'LXX'
    if int(positive_int[-2]) == 8:
        return 'LXXX'
    if int(positive_int[-2]) == 9:
        return 'XC'


def hundreds_conversion(positive_int):
    """Convert the hundreds place of an integer to Roman numeral.

    >>> hundreds_conversion(400)
    'CD'
    >>> hundreds_conversion(900)
    'CM'

    PARAM: positive_int[-3], an integer in the range of [0, 9]
    PRECONDITION: positive_int[-3] must be an integer in the range of [0, 9]
    POSTCONDITION: converts the hundreds place integer to the Roman numeral
    RETURN: converted hundreds place of an integer as Roman numeral"""
    positive_int = str(positive_int)
    if int(positive_int[-3]) < 4:
        return 'C' * int(positive_int[-3])
    if int(positive_int[-3]) == 4:
        return 'CD'
    if int(positive_int[-3]) == 5:
        return 'D'
    if int(positive_int[-3]) == 6:
        return 'DC'
    if int(positive_int[-3]) == 7:
        return 'DCC'
    if int(positive_int[-3]) == 8:
        return 'DCCC'
    if int(positive_int[-3]) == 9:
        return 'CM'


def thousands_conversion(positive_int):
    """Convert the thousands place of an integer to Roman numeral.

    >>> thousands_conversion(1000)
    'M'
    >>> thousands_conversion(10000)
    'MMMMMMMMMM'

    PARAM: positive_int[-4], an integer in the range of [0, 10]
    PRECONDITION: positive_int[-4] must be an integer in the range of [0, 10]
    POSTCONDITION: converts the thousands place integer to the Roman numeral
    RETURN: converted thousands place of an integer as Roman numeral"""
    positive_int = str(positive_int)
    if int(positive_int[-4]) > 0:  # If the thousands place has anything greater than 0, return M multiplied by value
        return 'M' * int(positive_int[-4])
    elif int(positive_int) == 10000:  # If the input is 10,000 then it will return 'M' * 10, the maximum value
        return 'M' * 10


def main():
    """Drives the function."""
    print(convert_to_roman_numeral(9999))
    doctest.testmod()


if __name__ == '__main__':
    main()
