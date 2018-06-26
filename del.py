#!/usr/bin/python3

# This contains misc system services.
import sys

# Delete operation.
try:
    dieter = [ 4, 5, 11, 43 ]
    print('dieter =', dieter)
    del dieter[2]
    print('dieter =', dieter)
    del dieter
    print('dieter =', dieter)
    print("Doesn't get here!")
except NameError as x:
    print("*** Name", x, "undefined ***")

dieter = 'hunter'
print('dieter =', dieter)
