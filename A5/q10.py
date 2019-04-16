"""Question 10."""

# Jacky Zheng
# Gray Chen

import doctest


def database_shared_headings(database_dict: dict) -> set:
    """Return the set of keys in all of the inner dictionaries.

    PARAM: database_dict, a dictionary with inner dictionary
    PRECONDITION: database_dict must be a dictionary with inner dictionary
    RETURN: a set of keys in all of the inner dictionaries
    """
    total_set = {head for head in database_dict[list(database_dict.keys())[0]]}  # Create a set from entire database
    for scientist in database_dict:
        scientist_set = set([head for head in database_dict[scientist]])  # Create a set from each scientist
        total_set = scientist_set.intersection(total_set)  # Compare to total set and intersection them
    return total_set


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
