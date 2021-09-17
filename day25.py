#!/usr/bin/env python3

from itertools import permutations, combinations, combinations_with_replacement

elements = ['Red', 'Green', 'Blue', 'Yellow', 'Black']

# generates a list of all possible permutations with no repeated elements of size 2
print(list(permutations(elements, 2)))

# generates a list of all possible combinations in sorted order with elements of size 3
print(list(combinations(elements, 3)))

# generates a list of all possible combinations in sorted order with elements of size 3
print(list(combinations_with_replacement(elements, 3)))
