#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = str(number)
p = ld[-1]
if number < 0:
    p = '-'+p
f = int(p)
s = ''
if f > 5:
    s = 'and is greater than 5'
elif f == 0:
    s = 'and is 0'
elif f < 6 and f != 0:
    s = 'and is less than 6 and not 0'
print(f"Last digit of {number} is {p} {s}")
