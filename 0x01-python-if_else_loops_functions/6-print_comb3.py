#!/usr/bin/python3
for i in range(100):
    if i < 10:
        i = f'0{i}'
    if str(i) < str(i)[::-1]:
        print('{}'.format(i), end=', ' if int(i) < 89 else '\n')
