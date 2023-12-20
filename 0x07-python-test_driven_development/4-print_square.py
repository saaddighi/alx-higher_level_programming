#!/usr/bin/python3

"""a function that prints a square"""


def print_square(size):
    """if size is not an integer raise error"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    """if size is less then 0 raise an error"""
    if size < 0:
        raise ValueError('size must be >= 0')
    """if size is a float and is less than 0 raise error"""
    if isinstance(size, float) is True and size < 0:
        raise TabError('size must be an integer')
    for i in range(size):
        p = '#'*size
        print(p)
