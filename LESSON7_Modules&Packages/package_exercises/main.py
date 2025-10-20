# main.py
from helpers.string import shout
from helpers.math import area

length = 5
width = 8
result = area(length, width)

message = f"the area of a {length}-by-{width} rectangle is {result}"
print(shout(message))