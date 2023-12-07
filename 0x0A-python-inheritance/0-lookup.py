#!/usr/bin/python3
def lookup(obj):
    """a function that returns a list of
    available attributes and methods of an object"""
    l= []
    l.append(dir(obj))
    return l
