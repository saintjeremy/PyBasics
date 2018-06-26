#!/usr/bin/python3

# Dictionaries map keys to values.

dieter = { 'mike': 456, 'bill': 399, 'sarah': 521 }

# Subscripts.
try:
    print(dieter)
    print(dieter['bill'])
    print(dieter['nora'])
    print("Won't see this!")
except KeyError as rest:
    print("Lookup failed:", rest)
print()

# Entries can be added, udated, or deleted.
dieter['bill'] = 'Sopwith Camel'
dieter['tuna'] = 2233
del dieter['mike']
print(dieter)
print()

# Get all the keys.
print(dieter.keys())
for k in dieter.keys():
    print(k, "=>", dieter[k])
print()

# Test for presence of a key.
for t in [ 'zingo', 'sarah', 'bill', 'tuna' ]:
    print(t,end=' ')
    if t in dieter:
        print('=>', dieter[t])
    else:
        print('is not present.')

