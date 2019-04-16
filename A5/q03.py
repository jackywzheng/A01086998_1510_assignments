"""Question 3."""

# Jacky Zheng
# Gray Chen

import doctest


def backup(filename: str):
    """Create a backup file with same contents as filename.

    PARAM: filename, a string of an existing filename in same directory
    PRECONDITION: filename must be a string
    POSTCONDITION: a created .bak file containing the contents of the filename

    >>> backup("doesntexist.exe")
    doesntexist.exe was not found.
    """
    try:
        with open(filename) as file_object:
            content = file_object.read()
        backup_filename = filename.split('.')  # Splits file name and extension into a list
        backup_filename[1] = '.bak'  # Replace extension with .bak
        backup_filename = ''.join(backup_filename)  # Rejoin list into a string with .bak extension
        with open(backup_filename, 'w') as file_object:
            file_object.write(content)
        print('generated', backup_filename)
    except FileNotFoundError:
        print(filename, 'was not found.')


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
