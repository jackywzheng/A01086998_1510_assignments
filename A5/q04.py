"""Question 4."""

# Jacky Zheng
# Gray Chen

import doctest


def selection_sort(a_list: list) -> list:
    """Sort a list from lowest to highest.

    PARAM: a_list, a non-empty list of sortable items
    PRECONDITION: a_list must be a non-empty list of sortable items
    RETURN: a sorted list from lowest to highest

    >>> selection_sort([3, 5, 1, 9, -4])
    [-4, 1, 3, 5, 9]

    >>> selection_sort (['d', 'a', 'c', 'b', 'e'])
    ['a', 'b', 'c', 'd', 'e']
    """
    if type(a_list) is not list or len(a_list) == 0:
        raise ValueError("a_list must be a list and not empty!")
    a_list_copy = a_list.copy()
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            if a_list_copy[j] < a_list_copy[i]:
                smallest = a_list_copy[j]
                a_list_copy[j], a_list_copy[i] = a_list_copy[i], smallest
    return a_list_copy


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
