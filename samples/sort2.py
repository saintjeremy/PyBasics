#!/usr/bin/python3
# Read the lines of the input file and sort them in various ways.

import sys

def prlines(label, lines):
    print(label+":")
    for x in lines:
        print("   "+x)
    print()

lines=[]
while True:
    line = sys.stdin.readline()
    if not line:
        break
    lines.append(line[:-1])

prlines("Initial", lines)
lines.sort()
prlines("Sorted", lines)

# This function is for sorting on the second word in the line,
# case-insensitive.  It also shows an alternate way to call the system
# sort.
def second(line):
    return line.split()[1].lower()
bysecond = sorted(lines, key=second)
prlines("Sorted on second word, case insensitive", bysecond)

# Sort the lines by length.
lines.sort(key=lambda s: len(s))
prlines("Sorted by length", lines)

# Sort by the number of words, followed by the line itself.
# The comparison function returns a tuple, which will be compared by
# comparing the first thing, then the second if the first does not match.
def words_then_text(s):
    return (len(s.split()),s.lower())
lines.sort(key=words_then_text)
prlines("Sorted by number of words, then CI text", lines)
