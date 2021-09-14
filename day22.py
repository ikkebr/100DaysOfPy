#!/usr/bin/env python3

# Lets say we want to read a list of numbers from the user
numbers = input("Enter numbers separated by a space: ").split()

# Now numbers is a list of strings
# We can use the map function to apply a function to all elements of a sequence
# For instance, we can apply the function int to each element in the sequence:
int_numbers = map(int, numbers)

# We can then iterate over int_numbers and verify that all numbers are now int
for number in int_numbers:
    print(number, type(number))

# Another useful function is the filter function
# It allows us to filter elements from a sequence according to a boolean predicate
odd_numbers = filter(lambda x: x % 2 != 0, range(10))

# We can then iterate over odd_numbers and get only the elements that match our predicate
for number in odd_numbers:
    print(number, end=" ")