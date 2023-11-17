#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(chr(ord('{}'.format(char)) - 32), end=' ' if char == ' ' else "")
