"""
Defines an empty Rectangle class.
"""


class Rectangle:
    """intiating and creating private attribute
       named width and """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height 
    """proprety width(self) to retrieve width """
    
    @property
    def width(self):
        return self._width
    
    """property setter def width(self, value): to set it"""
    @width.setter
    def width(self, value):
        if isinstance(value,int) == True:
            pass
        else:
            TypeError('width must be an integer')
        if value < 0:
            ValueError('width must be >= 0')
        self._width = value
    """property def height(self): to retrieve it"""
    @property
    def height(self):
        return self._height
    """proprety setter def height(self, value): to set it"""
    @height.setter
    def height(self, value):
        if isinstance(value,int) == True:
            pass
        else:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
           