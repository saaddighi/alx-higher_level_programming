#!/usr/bin/python3
def taks(argument):
    a = len(argument)
    if a == 1:
        a = f'{a} argument:'
    elif a == 0 :
        a = f'{a} arguments.'
    else:
        a = f'{a} arguments:'
    for i in argument :
        g = argument.index(i) + 1
        t = str(g)
        s = f'{t} : {argument}'
    return print(f"{a} \n {s} \n")  
        