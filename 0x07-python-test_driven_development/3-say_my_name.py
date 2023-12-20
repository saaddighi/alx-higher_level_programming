#!/usr/bin/python3

"""a function that return the first and last name"""

def say_my_name(first_name, last_name=""):
    """raise exeption if first name not a string"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    """raise exeption if last name not a string"""
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    return print(f'My name is {first_name} {last_name}')
