#!/usr/bin/env python3

# a non-recursive version of the anagram function
def anagram(seq):
    return seq == seq[::-1]

print( anagram("arara") ) # True
print( anagram("banana") ) # False