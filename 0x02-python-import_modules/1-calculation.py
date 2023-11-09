#!/usr/bin/python3
if __name__ == '__main__':
    a = 10
    b = 5
    
    def add(a,b):
        p = a + b 
        return '{} + {} = {}'.format(a,b,p)
    def sub(a,b):
        p = a - b
        return '{} - {} = {}'.format(a,b,p)
    def div(a,b):
        p = a / b
        return '{} / {} = {}'.format(a,b,p)
    def mul(a,b):
        p = a * b
        return '{} * {} = {}'.format(a,b,p)
    def calculator_1():
        return print(add(a,b) + '\n' + sub(a,b) + '\n' + div(a,b) + '\n' + mul(a,b))
calculator_1()