#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x = x
    except:
        x = x
    print(my_list[0:x+1],'\n')
