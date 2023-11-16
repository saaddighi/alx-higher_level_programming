#!/usr/bin/python3
p = []
def islower(c):
    for i in range(ord('a'), ord('z')+1):
        p.append(chr(i))
    if c in p:
        True
    else:
        False
