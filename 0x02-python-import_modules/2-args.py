#!/usr/bin/python3

if __name__ == '__main__':    
    
    def taks():
        argument = __builtins__.argv[:1]
        a = ''
        r = 0
        if argument != '':
            
            t = argument.split(' ')
            a = len(t)
            if a == 1:
                a = f'{a} argument:'
            elif a == 0 :
                a = f'{a} arguments.'
            elif argument == 0:
                a = f'{a} arguments:'
            print(a)
            for i in t:
                l = i
                r = r+1
                print(f'{r} : {l}')
        
        
        
        
        
taks()
        