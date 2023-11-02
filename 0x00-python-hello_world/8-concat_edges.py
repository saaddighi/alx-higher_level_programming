#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = (str[str.index('object'):str.index('lan')] + (str[str.index('with'):str.index('very')]) + (str[0:6]))
print(str)
