"""Convert alphabet letters in a phone number to corresponding numbers. """

# Jacky Zheng
# A01086998
# 01/30/19

import doctest


def number_translator():
    """Return the telephone number with any alphabetical numbers translated into their numerical equivalent.
    PRE-CONDITION: phone_number, user must input a string in the format of XXX-XXX-XXXX
    POST-CONDITION: prints the phone number with all letters converted to numerical equivalent"""
    phone_number = input('Enter a 10-character telephone number in the form of XXX-XXX-XXXX')
    phone_number = phone_number.lower()
    phone_number = phone_number.strip()
    translated = []
    translated.append(letter_appender(phone_number[0]))
    translated.append(letter_appender(phone_number[1]))
    translated.append(letter_appender(phone_number[2]))
    translated.append(letter_appender(phone_number[3]))
    translated.append(letter_appender(phone_number[4]))
    translated.append(letter_appender(phone_number[5]))
    translated.append(letter_appender(phone_number[6]))
    translated.append(letter_appender(phone_number[7]))
    translated.append(letter_appender(phone_number[8]))
    translated.append(letter_appender(phone_number[9]))
    translated.append(letter_appender(phone_number[10]))
    translated.append(letter_appender(phone_number[11]))
    # Print function below concatenates all the characters together
    print(translated[0] + translated[1] + translated[2] + translated[3] + translated[4] + translated[5] +
          translated[6] + translated[7] + translated[8] + translated[9] + translated[10] + translated[11])


def letter_appender(letter):
    """Check if the letter is in a string and return the corresponding number or symbol.

    >>> letter_appender('a')
    '2'
    >>> letter_appender('z')
    '9'

    PARAMETER: letter, a string in the range of [a, z]
    PRE-CONDITION: letter, a string in the range of [a, z]
    RETURN: corresponding number or symbol"""
    if letter in 'abc':  # You can do this instead of coding 'a' or 'b' or 'c'
        return '2'
    elif letter in 'def':
        return '3'
    elif letter in 'ghi':
        return '4'
    elif letter in 'jkl':
        return '5'
    elif letter in 'mno':
        return '6'
    elif letter in 'pqrs':
        return '7'
    elif letter in 'tuv':
        return '8'
    elif letter in 'wxyz':
        return '9'
    else:
        return letter  # Returns the dashes and numbers if there were any in the input


def main():
    """Drives the function."""
    number_translator()
    doctest.testmod()


if __name__ == '__main__':
    main()
