"""Convert alphabet letters in a phone number to corresponding numbers."""

# Jacky Zheng
# A01086998
# 01/30/19

translated = []


def number_translator():
    """Return the telephone number with any alphabetical numbers translated into their numerical equivalent.
    PARAMETER: phone_number, a string in the format of XXX-XXX-XXXX
    PRE-CONDITION: phone_number must be a string in the format of XXX-XXX-XXXX
    POST-CONDITION: prints the phone number with all letters converted to numerical equivalent"""
    phone_number = input('Enter a 10-character telephone number in the form of XXX-XXX-XXXX')
    phone_number = phone_number.lower()
    phone_number = phone_number.strip()
    letter_appender(phone_number[0])
    letter_appender(phone_number[1])
    letter_appender(phone_number[2])
    letter_appender(phone_number[3])
    letter_appender(phone_number[4])
    letter_appender(phone_number[5])
    letter_appender(phone_number[6])
    letter_appender(phone_number[7])
    letter_appender(phone_number[8])
    letter_appender(phone_number[9])
    letter_appender(phone_number[10])
    letter_appender(phone_number[11])
    # Print function below concatenates all the characters together
    print(translated[0] + translated[1] + translated[2] + translated[3] + translated[4] + translated[5] +
          translated[6] + translated[7] + translated[8] + translated[9] + translated[10] + translated[11])


def letter_appender(letter):
    """Check if the letter is in a string and append the corresponding number to the list.
    PARAMETER: letter, a string in the range of [a, z]
    PRE-CONDITION: letter, a string in the range of [a, z]
    POST-CONDITION: appends the corresponding number to the list"""
    if letter in 'abc':  # You can do this instead of coding 'a' or 'b' or 'c'
        translated.append('2')
    elif letter in 'def':
        translated.append('3')
    elif letter in 'ghi':
        translated.append('4')
    elif letter in 'jkl':
        translated.append('5')
    elif letter in 'mno':
        translated.append('6')
    elif letter in 'pqrs':
        translated.append('7')
    elif letter in 'tuv':
        translated.append('8')
    elif letter in 'wxyz':
        translated.append('9')
    else:
        translated.append(letter)  # Appends the dashes and numbers in the input as they were


def main():
    number_translator()


if __name__ == '__main__':
    main()
