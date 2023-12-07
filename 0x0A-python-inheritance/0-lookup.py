#!/usr/bin/python3
"""a function that returns a list of
available attributes and methods of an object
"""
def lookup(obj):
    """we creat a list variable then append the 
    output of dir(obj) in it"""
    l= []
    l.append(dir(obj))
    return l
