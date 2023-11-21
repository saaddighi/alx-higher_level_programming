#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side of the square.
        """
        
        """the value of size of square
           must be an interger"""
        try:
            if isinstance(size,int) is True:
                pass
        except:
            raise TypeError("size must be an integer")
        
        """the length of the side of square must be
           bigger then 0"""
        
        try:
            if size > 0:
                pass
        except:
            raise ValueError("size must be >= 0")
        self.__size = size
