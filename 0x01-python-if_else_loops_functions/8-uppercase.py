#!/usr/bin/python3
def uppercase(str):    
    for char in str:
        if char.islower() is True :   
            char = chr(ord((char)) - 32)
        print(char,end='')



