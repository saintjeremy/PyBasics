#!/usr/bin/python3

# A python list.
dieter = [ 'The', 'answer', 'to', 'your', 'question', 'is', 24 ]
print ('A:', dieter)

# Subscript, as strings.  Returns an item from the list.
print ('B:', dieter[0], dieter[2], dieter[6], dieter[-1], dieter[-4])

# Ranges create a "slice" -- a sublist.
print ('C:', dieter[2:5], dieter[-6:-3], dieter[4:5], dieter[3:3])

# Individual items may be replaced.
dieter[1] = 'response'
dieter[-1] = dieter[-1] + 200
dieter[-3] = 'query'
print ('D:', dieter)

# Assignment to slices is allowed, and can change the list size.
dieter[0:2] = [ 'An', 'unlikely', 'answer' ]
dieter[-1:-1] = [ 'a', 'conservative' ]
print ('E:', dieter)

# Sublists are allowed.
mike = [ 3, 4, ['and', 'also', 'a'], 52]
print ('F:', mike)
mike[0] = [2, '+', 1]
mike[2] = 11
print ('G:', mike)

dieter[1:3] = [dieter[1:3]]
dieter[-1:] = [mike]
print ('H:', dieter)

print ('dieter has', len(dieter), 'entries.')
