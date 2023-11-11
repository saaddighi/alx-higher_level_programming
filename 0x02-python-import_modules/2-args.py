#!/usr/bin/python3

if __name__ == '__main__':    
    
    def taks(argument):
        argument = str(argument)
        t = argument.split(' ')
        r = 0
        
        a = len(t)
        if a == 1:
            a = f'{a} argument:'
        elif a == 0 :
            a = f'{a} arguments.'
        else:
            a = f'{a} arguments:'
        print(a)
        for i in t:
            l = i
            r = r+1
            print(f'{r} : {l}')
        