#!/usr/bin/env python3

# recursive functions in Python are just like regular functions
def anagram(sequence):

    # we have a base case
    if not sequence:
        return True
    
    # and we have a recursive case
    if sequence[0] == sequence[-1]:
        return anagram(sequence[1:-1])

    return False

print(anagram("ARARA")) # True
print(anagram([1,2,1])) # True
print(anagram((3.1, 2.0, 2.0, 3.1))) # True
print(anagram("Henrique")) # False