#!/usr/bin/python3

# Several other operations on lists.

dieter = [ 'Alice', 'goes', 'to', 'market' ]
print ('A:', dieter)

dieter.extend([ 'with', 'Mike' ])
print ('B:', dieter)

last = dieter.pop()
dieter.append('dieter')

print ('C:', dieter)

print ('So much for Mike.')
print ('There are', len(dieter), 'items in dieter.')
print ('The word market is located at position', dieter.index('market'))

dieter = [ 'On', 'Tuesday,' ] + dieter
print ('D:', dieter)

dieter.reverse()
print ('E:', dieter)

dieter.sort()
print ('F:', dieter)
