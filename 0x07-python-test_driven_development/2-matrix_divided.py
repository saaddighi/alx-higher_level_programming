#!/usr/bin/python3

def matrix_divided(matrix, div):
    for i in matrix:
        while matrix[matrix.index(i)] < len(matrix):
            if len(i) != len(matrix[matrix.index(i)+1]):
                raise type('Each row of the matrix must have the same size')
    if div not in [int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        ZeroDivisionError('division by zero')  

    for i in matrix: 
        for d in i:
            if type(d) not in [int,float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')            
        return print(d / div)

