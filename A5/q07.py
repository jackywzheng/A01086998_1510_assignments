"""Question 7."""

# Jacky Zheng
# Gray Chen

import doctest
import re


def password_validator(password: str) -> bool:
    """Validate whether a password is strong or not.

    PARAM: password, a string
    PRECONDITION: password must be a string
    RETURN: True if password is strong, else False

    >>> password_validator('helloThere3')
    True

    >>> password_validator('hellothere')
    False
    """
    uppercase_regex = re.compile(r"[A-Z]+")
    lowercase_regex = re.compile(r"[a-z]+")
    digit_regex = re.compile(r"\d+")

    if len(password) < 8:
        return False
    if not uppercase_regex.findall(password):
        return False
    if not lowercase_regex.findall(password):
        return False
    if not digit_regex.findall(password):
        return False
    else:
        return True


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
