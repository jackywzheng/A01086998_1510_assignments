def convert_to_roman_numeral(positive_int):
    print(thousands_conversion(positive_int) + hundreds_conversion(positive_int)
          + tens_conversion(positive_int) + ones_conversion(positive_int))


def ones_conversion(positive_int):
    positive_int = str(positive_int)
    if int(positive_int[-1]) < 4:
        return 'I' * int(positive_int[-1])
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
    positive_int = str(positive_int)
    return 'M' * int(positive_int[-4])


def main():
    convert_to_roman_numeral(4994)


if __name__ == '__main__':
    main()
