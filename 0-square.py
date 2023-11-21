#!/usr/bin/python3
class Square:
    leg_lent = 4
    
    def __init__(self):
        self.dict = {}
my_square = Square()
print(type(my_square))
print(my_square.__dict__)