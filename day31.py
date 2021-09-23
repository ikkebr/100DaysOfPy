#!/usr/bin/env python3

numbers = [1, 2, 3, 4, 5]

# is_even is a boolean predicate that returns True if n is even
# or False otherwise.
def is_even(n):
    return n % 2 == 0


# the filter function uses a boolean predicate to remove elements from a sequence
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# we can also use lambda functions as predicates
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(list(odd_numbers))
