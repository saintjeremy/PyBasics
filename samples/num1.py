#!/usr/bin/python3
# Some calculations.  Note the lack of semicolons.  Statements end at the end
# of the line.  Also, variables need not start with a special symbol as in
# perl and some other Unix-bred languages.
dieter = 18
barney = dieter = 44;			# Case sensistive.
bill = (dieter + barney * dieter - 10)
alice = 10 + bill / 100			# Regular division does not truncate.
alice2 = 10 + bill // 100		# But the // operator provides int div.
frank = 10 + float(bill) / 100
print("dieter =", dieter)
print("dieter =", dieter)
print("bill =", bill)
print("alice =", alice)
print("alice2 =", alice2)
print("frank =", frank )
print()

# Each variable on the left is assigned the corresponding value on the right.
dieter, alice, frank = 2*alice, dieter - 1, bill + frank
print("dieter =", dieter)
print("alice =", alice)
print("frank =", frank )
print()

# Exchange w/o a temp.
dieter, alice = alice, dieter
print("dieter =", dieter)
print("alice =", alice)
print()

# Python allows lines to be continued by putting a backslash at the end of
# the first part.  
dieter = bill + alice + frank - \
       barney
print("dieter =", dieter)
print()

# The compiler will also combine lines when the line break in contained
# in a grouping pair, such as parens.
joe = 3 * (dieter +
	bill - alice)
print ("joe =", dieter)
