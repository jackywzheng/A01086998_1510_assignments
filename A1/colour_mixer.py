def colour_mixer():
    """Print the secondary colour given two primary colours.

    A function that prints the associated secondary colour when you combine two primary colours.
    PARAM: string, a primary colour
    PRE-CONDITION: string must be a primary colour (red, blue or yellow)
    POST-CONDITION: print the secondary colour of two primary colours"""

    colour_1 = input('What is your first primary colour? (red, blue, or yellow)')
    colour_1 = colour_1.lower()
    colour_2 = input('What is your second primary colour? (red, blue, or yellow)')
    colour_2 = colour_2.lower()

    if colour_1 == 'red' and colour_2 == 'blue' or colour_1 == 'blue' and colour_2 == 'red':
        print('Your secondary colour is purple!')
    elif colour_1 == 'blue' and colour_2 == 'yellow' or colour_1 == 'yellow' and colour_2 == 'blue':
        print('Your secondary colour is green!')
    elif colour_1 == 'yellow' and colour_2 == 'red' or colour_1 == 'red' and colour_2 == 'yellow':
        print('Your secondary colour is orange!')
    else:
        print('You did not pick two primary colours, or you picked the same colour!')


def main():
    colour_mixer()


if __name__ == '__main__':
    main()
