"""Mix two primary colours to generate a secondary colour."""

# Jacky Zheng
# A01086998
# 01/30/19
import doctest


def colour_mixer():
    """Print the secondary colour given two primary colours.
    PRECONDITION: colour_1, user must input a primary colour
    PRECONDITION: colour_2, user must input a different primary colour than colour_1
    POSTCONDITION: prints the secondary colour of two primary colours"""

    colour_1 = input('What is your first primary colour? (red, blue, or yellow)')
    colour_1 = colour_1.lower()
    colour_1 = colour_1.strip()
    colour_2 = input('What is your second primary colour? (red, blue, or yellow)')
    colour_2 = colour_2.lower()
    colour_2 = colour_2.strip()
    print(colour_mixer_helper(colour_1, colour_2))


def colour_mixer_helper(colour_1, colour_2):
    """Print the secondary colour given two primary colours.

    >>> colour_mixer_helper('red', 'blue')
    'Your secondary colour is purple!'
    >>> colour_mixer_helper('red', 'red')
    'You did not pick two primary colours, or you picked the same colour!'

    PARAM: colour_1, 'red', 'blue', or 'yellow'
    PARAM: colour_2, 'red', 'blue', or 'yellow'
    PRECONDITION: colour_1 must be 'red', 'blue', or 'yellow'
    PRECONDITION: colour_1 must be 'red', 'blue', or 'yellow'
    RETURN: the secondary colour of two primary colours or an error message"""

    if colour_1 == 'red' and colour_2 == 'blue' or colour_1 == 'blue' and colour_2 == 'red':
        return 'Your secondary colour is purple!'
    elif colour_1 == 'blue' and colour_2 == 'yellow' or colour_1 == 'yellow' and colour_2 == 'blue':
        return 'Your secondary colour is green!'
    elif colour_1 == 'yellow' and colour_2 == 'red' or colour_1 == 'red' and colour_2 == 'yellow':
        return 'Your secondary colour is orange!'
    else:
        return 'You did not pick two primary colours, or you picked the same colour!'


def main():
    colour_mixer()
    doctest.testmod()


if __name__ == '__main__':
    main()
